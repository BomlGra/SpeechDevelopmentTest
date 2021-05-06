from . import BaseModel
from peewee import *
import datetime

    
class Question(BaseModel):
    text = CharField(max_length=1024)
    created_at = DateTimeField(default=datetime.datetime.now)