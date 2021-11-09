# -*- coding: utf-8 -*-

# FastAPI
from fastapi.routing import APIRouter
from fastapi import status, Body

# Project
from app.models import User, UserRegister

router = APIRouter()


@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["users"],
)
def sing_up(user: UserRegister = Body(...)):
    """
    This endpoint register a new user in the app.
    Parameters:
        - Request body parameter:
            - user: UserRegister
    Returns a json with the basic user information.
    """
    user_dict = user.dict()
    user_dict.pop("password")
    return User(**user_dict)


@router.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["users"],
)
def login():
    pass
