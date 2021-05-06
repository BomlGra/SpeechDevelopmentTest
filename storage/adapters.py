from SpeechDevelopmentTest.protos.storage import storage_pb2
from models.question import Question
from models.report import Report
from models.audio import Audio
from google.protobuf.timestamp_pb2 import Timestamp
import datetime


class QuestionAdapter:
    @staticmethod
    def to_grpc(question):
        return storage_pb2.Question(
            question_id=question.id,
            text=question.text,
        )
        
class ReportAdapter:
    @staticmethod
    def to_grpc(report):
        print(report.created_at)
        print(type(report.created_at))
        t = datetime.datetime.now().timestamp()
        seconds = int(t)
        nanos = int(t % 1 * 1e9)
        timestamp_created_at = Timestamp(seconds=seconds, nanos=nanos)
        print(timestamp_created_at)
        return storage_pb2.Report(
            phonetic_score=report.phonetic_score,
            grammar_score=report.grammar_score,
            vocabular_score=report.vocabular_score,
            coherent_speech_score=report.coherent_speech_score,
            created_at=timestamp_created_at,
        )
        
    @staticmethod
    def from_grpc(report):
        report = Report(
            phonetic_score=report.phonetic_score,
            grammar_score=report.grammar_score,
            vocabular_score=report.vocabular_score,
            coherent_speech_score=report.coherent_speech_score,
        )
        return report   


class AudioAdapter:
    # @staticmethod
    # def to_grpc(report):
    #     return storage_pb2.Audio(
    #         phonetic_score=report.phonetic_score,
    #         grammar_score=report.grammar_score,
    #         vocabular_score=report.vocabular_score,
    #         coherent_speech_score=report.coherent_speech_score,
    #         created_at=timestamp_created_at,
    #     )
        
    @staticmethod
    def from_grpc(audio):
        return Audio(
            attempt=audio.attempt_id,
            question=audio.question_id,
        )