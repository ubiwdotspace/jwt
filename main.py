from app.core import JWTModule,SignModule
from config import Config
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
from app.routes.jwt import router as jwt_router
app = FastAPI()

# Gắn router vào FastAPI app
app.include_router(jwt_router, prefix='/api/v1', tags=['JWT'])

if __name__ == "__main__":

    uvicorn.run("main:app", host="127.0.0.1", port=8000)