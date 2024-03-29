# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import common_pb2 as common__pb2
import video_creator_pb2 as video__creator__pb2
import video_pb2 as video__pb2


class VideoCreatorUserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/internal_api.VideoCreatorUser/Create',
                request_serializer=video__pb2.VideoRequest.SerializeToString,
                response_deserializer=video__creator__pb2.VideoCreateResponse.FromString,
                )
        self.UpdateInfo = channel.unary_unary(
                '/internal_api.VideoCreatorUser/UpdateInfo',
                request_serializer=video__creator__pb2.VideoUpdateRequest.SerializeToString,
                response_deserializer=common__pb2.StatusResponse.FromString,
                )
        self.GetUploadLink = channel.unary_unary(
                '/internal_api.VideoCreatorUser/GetUploadLink',
                request_serializer=video__pb2.VideoRequest.SerializeToString,
                response_deserializer=common__pb2.StatusResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/internal_api.VideoCreatorUser/Delete',
                request_serializer=video__pb2.VideoRequest.SerializeToString,
                response_deserializer=common__pb2.StatusResponse.FromString,
                )


class VideoCreatorUserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUploadLink(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VideoCreatorUserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=video__pb2.VideoRequest.FromString,
                    response_serializer=video__creator__pb2.VideoCreateResponse.SerializeToString,
            ),
            'UpdateInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateInfo,
                    request_deserializer=video__creator__pb2.VideoUpdateRequest.FromString,
                    response_serializer=common__pb2.StatusResponse.SerializeToString,
            ),
            'GetUploadLink': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUploadLink,
                    request_deserializer=video__pb2.VideoRequest.FromString,
                    response_serializer=common__pb2.StatusResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=video__pb2.VideoRequest.FromString,
                    response_serializer=common__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'internal_api.VideoCreatorUser', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VideoCreatorUser(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/internal_api.VideoCreatorUser/Create',
            video__pb2.VideoRequest.SerializeToString,
            video__creator__pb2.VideoCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/internal_api.VideoCreatorUser/UpdateInfo',
            video__creator__pb2.VideoUpdateRequest.SerializeToString,
            common__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUploadLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/internal_api.VideoCreatorUser/GetUploadLink',
            video__pb2.VideoRequest.SerializeToString,
            common__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/internal_api.VideoCreatorUser/Delete',
            video__pb2.VideoRequest.SerializeToString,
            common__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
