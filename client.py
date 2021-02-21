from __future__ import print_function

import random
import logging

import grpc

import recognizer_pb2
import recognizer_pb2_grpc


def gener():
    yield recognizer_pb2.Chunk(Content=bytes('test', encoding = 'utf-8'))

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = recognizer_pb2_grpc.NNetworkStub(channel)
        print('Hello :3')
        result = stub.GetAudio(gener())
        print(result.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()