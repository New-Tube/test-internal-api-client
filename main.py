from __future__ import print_function

import grpc

import test_pb2_grpc
import test_pb2


from fastapi import FastAPI
import uvicorn
import json

NAME = "Mrs. VS Code"

def run():
    try:
        with grpc.insecure_channel("internal-api:5050") as channel:
            stub = test_pb2_grpc.TestStub(channel)
            response = stub.Hello(test_pb2.HelloRequest(Name=NAME))
        return {"status": "success", "response": response.Message}
    except Exception as e:
        return {"status": "error", "message": str(e)}

    # return response.Message


app = FastAPI()


@app.get("/get")
def get():
    return {"response": json.dumps(run())}


@app.get("/")
def root():
    return {"Hello": "world"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info")
