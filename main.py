from app.core import JWTModule,SignModule
from config import Config
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import FastAPI,Depends
from fastapi_simple_rate_limiter import rate_limiter
import uvicorn
from app.routes.jwt import router as jwt_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
app.include_router(jwt_router, prefix='/api/v1', tags=['JWT'])
if __name__ == "__main__":

    uvicorn.run("main:app", host="127.0.0.1", port=8000)