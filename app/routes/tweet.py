# -*- coding: utf-8 -*-

# Python
from typing import List

# FastAPI
from fastapi.routing import APIRouter
from fastapi import status, Body

# Project
from app.models import Tweet


router = APIRouter()


@router.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets.",
    tags=["tweets"],
)
def home():
    results = []
    return results


@router.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a new tweet.",
    tags=["tweets"],
)
def new_tweet(tweet: Tweet = Body(...)):
    return tweet


@router.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet.",
    tags=["tweets"],
)
def show_tweet():
    pass


@router.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update tweet",
    tags=["tweets"],
)
def update_tweet():
    pass


@router.delete(
    path="/tweets/{tweet_id}/delete",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a tweet.",
    tags=["tweets"],
)
def delete_tweet():
    pass
