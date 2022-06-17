from fastapi import FastAPI

from pytemplates.routes import all_routes

app = FastAPI()


app.include_router(
    all_routes.router,
    prefix="",
)


if __name__ == "__main__":
    app()
