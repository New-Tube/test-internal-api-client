FROM --platform=amd64 ubuntu:22.04

RUN apt-get update
RUN apt-get install -y python3.11 python3-pip
RUN pip install fastapi
RUN pip install "uvicorn[standard]"
RUN pip install grpcio
RUN pip install grpcio-tools

WORKDIR /app

COPY . .

EXPOSE 8080

ENTRYPOINT [ "python3", "main.py" ]
