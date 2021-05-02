# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ui_pb2 as ui__pb2


class NNetworkStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetScore = channel.unary_unary(
                '/NNetwork/GetScore',
                request_serializer=ui__pb2.Audios.SerializeToString,
                response_deserializer=ui__pb2.ResultReply.FromString,
                )


class NNetworkServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetScore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NNetworkServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetScore': grpc.unary_unary_rpc_method_handler(
                    servicer.GetScore,
                    request_deserializer=ui__pb2.Audios.FromString,
                    response_serializer=ui__pb2.ResultReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NNetwork', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NNetwork(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetScore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NNetwork/GetScore',
            ui__pb2.Audios.SerializeToString,
            ui__pb2.ResultReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AuthStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Registration = channel.unary_unary(
                '/Auth/Registration',
                request_serializer=ui__pb2.RegData.SerializeToString,
                response_deserializer=ui__pb2.Status.FromString,
                )
        self.Authentication = channel.unary_unary(
                '/Auth/Authentication',
                request_serializer=ui__pb2.AuthData.SerializeToString,
                response_deserializer=ui__pb2.Status.FromString,
                )


class AuthServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Registration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Authentication(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Registration': grpc.unary_unary_rpc_method_handler(
                    servicer.Registration,
                    request_deserializer=ui__pb2.RegData.FromString,
                    response_serializer=ui__pb2.Status.SerializeToString,
            ),
            'Authentication': grpc.unary_unary_rpc_method_handler(
                    servicer.Authentication,
                    request_deserializer=ui__pb2.AuthData.FromString,
                    response_serializer=ui__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Auth', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Auth(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Registration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Auth/Registration',
            ui__pb2.RegData.SerializeToString,
            ui__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Authentication(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Auth/Authentication',
            ui__pb2.AuthData.SerializeToString,
            ui__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
