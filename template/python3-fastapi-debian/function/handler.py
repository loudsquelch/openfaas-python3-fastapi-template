from fastapi import HTTPException
from pydantic import BaseModel
from typing import Dict

FUNCTION_NAME = 'templatefn'
FUNCTION_VERSION = '1.0.0'
FUNCTION_SUMMARY = "A function that does this"
FUNCTION_RESPONSE_DESC = "Definition of object returned by function"


class RequestModel(BaseModel):
    data: Dict


class ResponseModel(BaseModel):
    data: Dict


def handle(req):
    """handle a request to the function
    Args:
        req (dict): request body
    """
    try:
        res = ResponseModel(data=req.data)
    except Exception:
        raise HTTPException(status_code=500, detail=f"An API Error occurred")
    return res
