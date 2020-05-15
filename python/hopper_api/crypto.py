from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import base64
import jwt

def generate_keys():
    privateKey = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return (privateKey.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1
    ), privateKey.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

def sign(obj, privateKey):
    return jwt.encode(obj, privateKey, 'RS256').decode('utf-8')    

def encode_key_base64(key):
    return base64.b64encode(key).decode('utf-8')

def decode_private_key_base64(b64):
    return base64.b64decode(b64.encode('utf-8'))

