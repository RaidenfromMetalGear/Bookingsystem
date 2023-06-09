
import os
import base64

def generate_secret_key():
    return base64.b64encode(os.urandom(24)).decode('utf-8')

secret_key = generate_secret_key()
print(secret_key)