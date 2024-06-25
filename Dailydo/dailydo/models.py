from sqlmodel import SQLModel, Field
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import Form
from pydantic import BaseModel

# Create Model
    # data model
    # table model
# Todo is a child class and will extend it's parent class SQLModel
# This model will use for both data validation and table creation(data model & table model)
class Todo(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    content : str = Field(index=True, min_length=3, max_length=54)
    is_completed : bool = Field(default=False)
    user_id : int = Field(foreign_key="user.id")

class User(SQLModel, table=True):
    id : int = Field(default=None, primary_key=True)
    username : str
    email : str
    password : str

class Register_User(BaseModel):
            username: Annotated[
            str,
            Form(),
        ]
            email: Annotated[
            str,
            Form(),
        ]
            password: Annotated[
            str,
            Form(),
        ]

class Token(BaseModel):
    access_token:str
    token_type:str
    

