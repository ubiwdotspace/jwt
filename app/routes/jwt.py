from fastapi import APIRouter, Depends, HTTPException, status, Query
from app.core import JWTModule, SignModule
from app.schemas import JWTModel
from config import Config
from eth_account.messages import encode_defunct
# Initialize Web3
from web3 import Web3
import requests
import json
from fastapi import Depends, FastAPI
from fastapi_simple_rate_limiter import rate_limiter
w3 = Web3(Web3.HTTPProvider(Config.RPC_ENDPOINT))
router = APIRouter()


class JWTRouter:
    @router.get("/get-msg")
    @rate_limiter(limit=1000, seconds=60)
    async def get_sign_message(address: str = Query(...)):
        try:
            message = SignModule.get_sign_msg(address=address)
            return {"message":message}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )
    @router.post("/get-jwt")
    @rate_limiter(limit=1000, seconds=60)
    async def get_jwt(request_data: JWTModel):
        try:
            signature = request_data.signature
            msg = request_data.msg
            live = SignModule.validate_nonce(msg)
            if(live):
            # signable_msg_from_hexstr = encode_defunct(text=msg)
            # signed_message =  w3.eth.account.sign_message(signable_msg_from_hexstr, private_key=key)
            # print(signed_message)
                signer = SignModule.get_address_of(signature,msg)   
                if(signer):
                    url = Config.RPC_ENDPOINT
                    signer = w3.to_checksum_address(signer)
                    payload = {
                        "jsonrpc": "2.0",
                        "method": "particle_aa_getSmartAccount",
                        "params": [
                            {
                            "name": "SIMPLE",
                            "version": "1.0.0",
                            "ownerAddress": signer
                            }
                        ]
                    }
                    headers = {
                        "accept": "application/json",
                        "content-type": "application/json",
                    }
                    response = requests.post(url, json=payload, headers=headers)   
                    data = json.loads(response.text)
                    smart_account_address = data["result"][0]["smartAccountAddress"]
                    payload = {"sub": smart_account_address}
                    token = JWTModule.create_jwt(payload)
                    return {"token": token}
            else:
                return {"signature": "expired"}    

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )
                           
                
        



