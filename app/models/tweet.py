# -*- coding: utf-8 -*-
# Python
from uuid import UUID
from datetime import datetime
from typing import Optional

# Pydantic
from pydantic import BaseModel, Field

# Project
from .user import User


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(..., max_length=256, min_length=1)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
