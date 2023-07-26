"""Server functions for this demo code."""

import logging

import grpc
from concurrent import futures

# import the generated classes
import publish_pb2
import publish_pb2_grpc

# import helpers to work with the received data.
import datum

logger = logging.getLogger(__name__)

logging.basicConfig(
    format="%(asctime)-15s %(levelname)s :: %(filename)s:%(lineno)s:%(funcName)s() :: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level="INFO",
)


class PublishServicer(publish_pb2_grpc.Publish):
    """PublishService derived from the generated
    publish_pb2_grpc.PublishServicer.
    """

    def PublishDatum(self, request, context):
        """Receive the value from the client and process it with a given
        handler. A confirmation object is created and returned to the
        caller.
        """
        response = publish_pb2.Confirmation()
        confirmation, value = datum.process_datum(request.datum)
        response.accepted = confirmation
        response.value = value
        return response


def serve():
    """Establish the server."""

    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # use the generated function `add_PublisherServicer_to_server` to add the
    # defined class to the created server
    publish_pb2_grpc.add_PublishServicer_to_server(PublishServicer(), server)

    # run the server on port 50051
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
