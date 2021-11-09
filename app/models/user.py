# -*- coding: utf-8 -*-

# Python
from typing import Optional
from datetime import date
from uuid import UUID

# pydantic
from pydantic import BaseModel, EmailStr, Field


class BaseUser(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birth_date: Optional[date] = Field(default=None)


class User(BaseUser):
    pass


class UserRegister(BaseUser):
    password: str = Field(..., min_length=8)
