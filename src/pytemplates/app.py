import os
import socket

import fastapi

from pytemplates.core.module1 import greet
from pytemplates.core.module2 import wish_farewell

app = fastapi.FastAPI()


@app.get("/")
async def root():
    return greet(user="PyTemplates User")


@app.get("/hello")
async def hello(user: str):
    return greet(user=user)


@app.get("/goodbye")
async def hello(user: str):
    return wish_farewell(user=user)


@app.get("/whoami")
async def whoami():
    return {
        "host_name": socket.gethostname(),
        "host_ip": socket.gethostbyname(socket.gethostname()),
        "process_id": os.getpid(),
    }


if __name__ == "__main__":
    app()
