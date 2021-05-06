from . import BaseModel
from .user import User
from .report import Report
from peewee import *

    
class Attempt(BaseModel):
    user = ForeignKeyField(User)
    report = ForeignKeyField(Report, null=True)