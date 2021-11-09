# -*- coding: utf-8 -*-
# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData

# Local
from config import settings


DB_URL = f'postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'

engine = create_engine(DB_URL)
meta = MetaData()
connection = engine.connect()
