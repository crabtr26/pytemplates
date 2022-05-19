import fastapi

from pytemplates import __version__
from pytemplates.core.module1 import greet
from pytemplates.core.module2 import wish_farewell

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return greet(user="PyTemplates User")

@app.get("/test")
async def test():
    hello = greet(user="PyTemplates User")
    message = f"{hello} PyTemplates has been installed successfully!"
    mypackage_info = f"pytemplates=={__version__}"
    pandas_info = f"fastapi=={fastapi.__version__}"
    print(message, mypackage_info, pandas_info)
    goodbye = wish_farewell(user="PyTemplates User")
    print(goodbye, "Thank you for using PyTemplates!")
    final_message = message, mypackage_info, pandas_info, goodbye, "Thank you for using PyTemplates!"
    return final_message

@app.post("/hello")
async def hello(user: str):
    return greet(user=user)

@app.post("/goodbye")
async def hello(user: str):
    return wish_farewell(user=user)

if __name__ == "__main__":
    app()

