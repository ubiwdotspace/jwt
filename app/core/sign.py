from web3 import Web3
from config import Config
from datetime import datetime
from hexbytes import HexBytes
from eth_account.messages import encode_defunct
import re

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(Config.RPC_ENDPOINT))

class SignModule:
    @staticmethod
    def validate_nonce(msg):
        match = re.search(r"nonce (\d+)", msg)
        if match:
            nonce = int(match.group(1))
            now = datetime.utcnow().timestamp()
            if now - nonce < 300:
                return True
            else:
                return False
            
    @staticmethod
    def get_nonce():
        """ Generates a nonce based on the current UTC timestamp. """
        return int(datetime.utcnow().timestamp())

    @staticmethod
    def get_address_of(signature, msg):
        """ Recovers the address from the signature and message. """
        message = encode_defunct(text=msg)
        _address = w3.eth.account.recover_message(message, signature=HexBytes(signature))
        return _address

    @classmethod
    def _get_sign_msg(cls, address, nonce):
        """ Generates a signed message with nonce and address. """
        return f"I'm signing to LinkPatron using nonce {nonce} by Smart Contract Wallet : {address}"

    @classmethod
    def get_sign_msg(cls, address):
        """ Public interface to get a signed message for a specific address. """
        _nonce = cls.get_nonce()
        return cls._get_sign_msg(address=address, nonce=_nonce)
