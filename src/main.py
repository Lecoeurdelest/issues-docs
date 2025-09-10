from fastapi import FastAPI
from controller import routers
import uvicorn

def main():

    app = FastAPI(
        title="Issue Documentation Service",
        description="API for managing issue documentation",
        version="1.0.0",
    )

    for router in routers:
        app.include_router(router)

    return app

app = main()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8008,
        reload=True
    )