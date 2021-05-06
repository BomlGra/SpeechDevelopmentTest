from . import BaseModel
from .attempt import Attempt
from .question import Question
from peewee import *


class Audio(BaseModel):
    attempt = ForeignKeyField(Attempt, backref='audious')
    question = ForeignKeyField(Question)
    path = CharField(max_length=25000)