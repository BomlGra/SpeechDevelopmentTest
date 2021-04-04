from models import BaseModel
from models.audio import Audio
from peewee import *


class Question(BaseModel):
    text = CharField(max_length=256)
    answer = ForeignKeyField(Audio)