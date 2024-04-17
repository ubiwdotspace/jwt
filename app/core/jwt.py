from authlib.jose import jwt
from authlib.jose.errors import DecodeError
from config import Config

class JWTModule:
        header = {"alg": "HS256"}
        secret = Config.JWT_SECRET
        @classmethod
        def create_jwt(cls, payload):
            token = jwt.encode(cls.header, payload, cls.secret)
            return token.decode("ascii") 
