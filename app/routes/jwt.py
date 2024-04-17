from fastapi import APIRouter, Depends, HTTPException, status, Query
from app.core import JWTModule, SignModule
from app.schemas import JWTModel
from config import Config
from eth_account.messages import encode_defunct
# Initialize Web3
from web3 import Web3
w3 = Web3(Web3.HTTPProvider(Config.RPC_ENDPOINT))
router = APIRouter()

class JWTRouter:
    @router.get("/get-msg")
    def get_sign_message(address: str = Query(...)):
        try:
            message = SignModule.get_sign_msg(address=address)
            return {"message":message}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )
    @router.post("/get-jwt")
    def get_jwt(request_data: JWTModel):
        try:
            signature = request_data.signature
            msg = request_data.msg
            live = SignModule.validate_nonce(msg)
            if(live):
            # signable_msg_from_hexstr = encode_defunct(text=msg)
            # signed_message =  w3.eth.account.sign_message(signable_msg_from_hexstr, private_key=key)
            # print(signed_message)
                signer = SignModule.get_address_of(signature,msg)
                # print(signer)
                
                if(signer):
                    payload = {"sub": "user1", "aud": ["audience"]}
                    payload["sub"] = signer
                    token = JWTModule.create_jwt(payload)
                    return {"token": token}
            else:
                return {"signature": "expired"}    

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )
                
        



