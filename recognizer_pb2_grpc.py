# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import recognizer_pb2 as recognizer__pb2


class NNetworkStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAudio = channel.stream_unary(
                '/NNetwork/GetAudio',
                request_serializer=recognizer__pb2.Chunk.SerializeToString,
                response_deserializer=recognizer__pb2.ResultReply.FromString,
                )


class NNetworkServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAudio(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NNetworkServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAudio': grpc.stream_unary_rpc_method_handler(
                    servicer.GetAudio,
                    request_deserializer=recognizer__pb2.Chunk.FromString,
                    response_serializer=recognizer__pb2.ResultReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NNetwork', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NNetwork(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAudio(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/NNetwork/GetAudio',
            recognizer__pb2.Chunk.SerializeToString,
            recognizer__pb2.ResultReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class FlaskStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetResult = channel.unary_unary(
                '/Flask/GetResult',
                request_serializer=recognizer__pb2.ResultReply.SerializeToString,
                response_deserializer=recognizer__pb2.UploadStatus.FromString,
                )


class FlaskServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FlaskServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetResult': grpc.unary_unary_rpc_method_handler(
                    servicer.GetResult,
                    request_deserializer=recognizer__pb2.ResultReply.FromString,
                    response_serializer=recognizer__pb2.UploadStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Flask', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Flask(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Flask/GetResult',
            recognizer__pb2.ResultReply.SerializeToString,
            recognizer__pb2.UploadStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
