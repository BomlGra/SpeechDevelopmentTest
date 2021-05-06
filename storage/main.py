from concurrent import futures
import logging

import grpc
from SpeechDevelopmentTest.protos.storage import storage_pb2
from SpeechDevelopmentTest.protos.storage import storage_pb2_grpc
from adapters import *
from models.question import Question
from models.attempt import Attempt
from models.report import Report
from models.user import User
from google.protobuf.empty_pb2 import Empty
from compressor import Compressor, ZipCompressor
import uuid
import os


AUDIO_DIRECTORY = '/Users/alpha/Projects/Students/shumak/SpeechDevelopmentTest/storage/files/'


class Storage(storage_pb2_grpc.StorageServicer):
    def __init__(self):
        self.compressor: Compressor = ZipCompressor()
         
    def GetQuestions(self, request, context):
        questions = list(Question.select())
        grpc_questions = list(map(QuestionAdapter.to_grpc, questions))
        return storage_pb2.GetQuestionsResponse(
            questions=grpc_questions,
        )

    def StartAttempt(self, request, context):
        attempt = Attempt.create(user=request.user_id)
        return storage_pb2.StartAttemptResponse(attempt_id=attempt.id)

    def UploadAudio(self, request, context):
    # rpc UploadAudio(UploadAudioRequest) returns (UploadAudioResponse);
        
        attempt = Attempt.get_by_id(request.audio.attempt_id)
        owner = attempt.user.id
        file_directory = AUDIO_DIRECTORY+str(owner)
        if not os.path.exists(file_directory):
            os.makedirs(file_directory)
        file_name = str(uuid.uuid4()) + '.wav'
        file_path = file_directory + '/' + file_name
        file = open(file_path, 'wb')
        file.write(request.audio.content)
        file.close()
        
        audio = AudioAdapter.from_grpc(request.audio)
        audio.attempt = attempt
        audio.path = file_path
        audio.save()
        
        return storage_pb2.UploadAudioResponse(
            audio_id=audio.id,
        )

    def AttachReportToAttempt(self, request, context):
        attempt = Attempt.get_by_id(request.attempt_id)
        report = ReportAdapter.from_grpc(request.report)
        report.save()
        attempt.report = report
        attempt.save()
        print('attempt: ', attempt)
        print('report: ', report)
        return Empty()

    def GetReportByAttempt(self, request, context):
        attempt = Attempt.get_by_id(request.attempt_id)
        print(attempt)
        report = ReportAdapter.to_grpc(attempt.report)
        print(report)
        return storage_pb2.GetReportByAttemptResponse(report=report)
    
    def GetAudiousInArchive(self, request, context):
        audious = list(Attempt.get_by_id(request.attempt_id).audious)
        archive_content = dict()
        for index, audio in enumerate(audious):
            with open(audio.path, 'rb') as file:
                content = file.read()
                archive_content['{}.wav'.format(index+1)] = content
        archive = self.compressor.compress(archive_content)
        return storage_pb2.GetAudiousInArchiveResponse(archive=archive)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    storage_pb2_grpc.add_StorageServicer_to_server(Storage(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Storage service started')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()