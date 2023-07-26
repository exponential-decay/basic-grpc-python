"""Client to provide example connectivity to the server."""
import json
import logging

import grpc


# import the generated classes
import publish_pb2
import publish_pb2_grpc

logger = logging.getLogger(__name__)

logging.basicConfig(
    format="%(asctime)-15s %(levelname)s :: %(filename)s:%(lineno)s:%(funcName)s() :: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level="INFO",
)


# open a gRPC channel
channel = grpc.insecure_channel("localhost:50051")

# create a stub (client)
stub = publish_pb2_grpc.PublishStub(channel)

data = {}
data["confirmation"] = True
data["value"] = "1.234"

# create a valid request message
datum = publish_pb2.Datum(datum=json.dumps(data))

# make the call
response = stub.PublishDatum(datum)

# et voilà
logger.info("Received confirmation: %s", response.accepted)
logger.info("Received value: %s", response.value)
