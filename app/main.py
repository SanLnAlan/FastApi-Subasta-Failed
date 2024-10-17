from fastapi import FastAPI, Response
from routers.operations import router as operations_router
from routers.users import router as users_router

app = FastAPI()

app.include_router(operations_router)
app.include_router(users_router)

@app.get("/")
def read_root():
    return Response("Server is running")


