# author: Justin Guese, 11.3.22, justin@datafortress.cloud
from fastapi import HTTPException
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, List

router = APIRouter()

# just as an example
class User(BaseModel):
    id: int
    name: str
    age: int
    colleagues: List[str]

class ResponseModel(BaseModel):
    data: Dict
    # user: User
    # otherStuff: str

@router.post("/", response_model = ResponseModel, tags=["Main Routes"])
def handle(request: Dict):
    """handle a request to the function
    Args:
        req (dict): request body
    """
    try:
        res = ResponseModel(data=request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(repr(e)))
    return res

@router.get("/", response_model = ResponseModel, tags=["Main Routes"])
def get():
    return ResponseModel(data={"message": "Hello from OpenFAAS!"})

# again just as an example, delete this if not required
@router.get("/users/{user_id}", response_model = User, tags=["Main Routes"])
def getUser(user_id: int):
    return User(id = user_id, name="Exampleuser", age=20, colleagues=["Colleague 1", "Colleague 2"])