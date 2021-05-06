# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Question(peewee.Model):
    text = CharField(max_length=1024)
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        table_name = "question"


@snapshot.append
class Audio(peewee.Model):
    question = snapshot.ForeignKeyField(index=True, model='question')
    path = CharField(max_length=25000)
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        table_name = "audio"


@snapshot.append
class Report(peewee.Model):
    phonetic_score = IntegerField()
    grammar_score = IntegerField()
    vocabulary_score = IntegerField()
    coherent_speech_score = IntegerField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        table_name = "report"


