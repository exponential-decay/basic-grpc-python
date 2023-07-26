# Basic gRPC in Python

Contains a minimal working example for rolling gRPC in Python.

Derived from: [basic-grpc-python][pyhton-1] and updated to Python 3 with some
example data relevant to my current work.

[pyhton-1]: https://github.com/ramananbalakrishnan/basic-grpc-python

For more details: [blog post][medium-1].

[medium-1]: https://medium.com/engineering-semantics3/a-simplified-guide-to-grpc-in-python-6c4e25f0c506
## Quickstart

```shell
git clone https://github.com/exponential-decay/basic-grpc-python
cd basic-grpc-python
pip install -r requirements.txt
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. publish.proto
python server.py
python client.py
```

## File reference
```
basic-grpc-python/
├── datum.py               # module containing a function
|
├── publish.proto          # protobuf definition file
|
├── publish_pb2_grpc.py    # generated class for server/client
├── publish_pb2.py         # generated class for message
|
├── server.py              # a server to expose the function
└── client.py              # a sample client
```
