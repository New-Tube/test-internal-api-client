from __future__ import print_function

import grpc

import user_pb2_grpc
import user_pb2


from fastapi import FastAPI
import uvicorn

from os import environ
from dotenv import load_dotenv

def run():
    try:
        with grpc.insecure_channel(environ.get("HOST")) as channel:
            stub = user_pb2_grpc.UserStub(channel)
            response = stub.Get(user_pb2.UserRequest(ID=1))
        return {"status": "success", "response": response.Message}
    except Exception as e:
        return {"status": "error", "message": str(e)}

app = FastAPI()


@app.get("/get")
def get():
    result = run()
    if result['status'] == 'success':
        return result['response']
    else:
        return result['message']


@app.get("/")
def root():
    return {"Hello": "world"}


if __name__ == "__main__":
    load_dotenv()
    print("Running on host:", environ.get("HOST"))
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info")
