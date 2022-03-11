# author: Justin Guese, 11.3.22, justin@datafortress.cloud
from os import environ
import glob
from fastapi import FastAPI
from function.handler import router

# reads in secrets to environment variables, such that they can be 
# easily used with environ["SECRET_NAME"]
def readSecretToEnv(secretpath):
    secretname = secretpath.split('/')[-1]
    with open(secretpath, "r") as f:
        environ[secretname] = f.read()
        
for secret in glob.glob("/var/openfaas/secrets/*"):
    readSecretToEnv(secret)

app = FastAPI()
app.include_router(router)