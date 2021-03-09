from concurrent import futures
import grpc
import recognizer_pb2
import recognizer_pb2_grpc

import time
import math
import logging

import speech_recognition as sr
from io import BytesIO



class RecognizerServicer(recognizer_pb2_grpc.NNetworkServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        pass

    def GetAudio(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        bytes_audio = None
        for chunk in request_iterator:
            bytes_audio = chunk.Content
        r = sr.Recognizer()
        audio_data1 = sr.AudioFile(BytesIO(bytes_audio))
        recognized_text = ''
        with audio_data1 as source1:
            audio1 = r.record(source1)
            recognized_text = r.recognize_google(audio1, language='ru-RU')
        print(recognized_text)
        return recognizer_pb2.ResultReply(message=recognized_text)
        # context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        # context.set_details('Method not implemented!')
        # raise NotImplementedError('Method not implemented!')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    recognizer_pb2_grpc.add_NNetworkServicer_to_server(
        RecognizerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()