from models import BaseModel
from models.user import User
from peewee import *
import datetime


class Audio(BaseModel):
    user = ForeignKeyField(User, backref='audio') # array of audio
    path = CharField(max_length=256)
