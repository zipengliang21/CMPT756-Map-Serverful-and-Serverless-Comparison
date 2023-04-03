#!/bin/bash

# Generates gRPC and protobuf python outputs.
protoc --python_out=proto_py                                          \
       --proto_path=proto                                             \
       `find proto -name *.proto`
