from . import BaseModel
from peewee import *
import datetime


class Report(BaseModel):
    phonetic_score = IntegerField()
    grammar_score = IntegerField()
    vocabular_score = IntegerField()
    coherent_speech_score = IntegerField()
    created_at = DateTimeField(default=datetime.datetime.now)
    