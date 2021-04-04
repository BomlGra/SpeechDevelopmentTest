from models import BaseModel
from peewee import *


class User(BaseModel):
    email = CharField(max_length=128)
    password = CharField(max_length=128)
    name = CharField(max_length=128)
    age = IntegerField()