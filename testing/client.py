from __future__ import print_function

import random
import logging

import grpc

import recognizer_pb2
import recognizer_pb2_grpc


def gener():
    audio_bytes = None
    with open('test.wav', 'rb') as audio_file:
        audio_bytes = audio_file.read()
    yield recognizer_pb2.Chunk(Content=audio_bytes)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('192.168.1.65:50051') as channel:
        stub = recognizer_pb2_grpc.NNetworkStub(channel)        
        result = stub.GetAudio(gener())
        print(result.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()