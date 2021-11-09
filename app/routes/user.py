# -*- coding: utf-8 -*-

# Python
from typing import List

# FastAPI
from fastapi.routing import APIRouter
from fastapi import status, Body

# Project
from app.models import User

router = APIRouter()


@router.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Users",
    tags=["users"],
)
def show_users():
    results = []
    return results


@router.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a single User",
    tags=["users"],
)
def show_user():
    pass


@router.delete(
    path="/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a user",
    tags=["users"],
)
def delete_user():
    pass


@router.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update user",
    tags=["users"],
)
def update_user():
    pass
