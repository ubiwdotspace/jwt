from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    JWT_SECRET = os.getenv("JWT_SECRET")
    RPC_ENDPOINT = os.getenv("RPC_ENDPOINT")