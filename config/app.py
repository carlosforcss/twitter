# -*- coding: utf-8 -*-

# FastAPI
from fastapi import FastAPI

# Project
from app.routes import user_router, auth_router, tweet_router


def create_app():
    app = FastAPI()
    app.include_router(user_router, prefix="/users")
    app.include_router(tweet_router, prefix="/tweets")
    app.include_router(auth_router, prefix="/auth")
    return app
