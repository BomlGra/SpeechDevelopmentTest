from models import BaseModel
from models.user import User
from peewee import *
import datetime


class Report(BaseModel):
    user = ForeignKeyField(User, backref='reports')
    date = DateField(default=datetime.datetime.now())
    score = IntegerField()