from common.models import BaseModel
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String


class ExampleModel(BaseModel):
    __tablename__ = "example"

    title = Column(String)
    maia = Column(String)
    juliana = Column(String)