# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class User(peewee.Model):
    
    class Meta:
        table_name = "user"


@snapshot.append
class Attempt(peewee.Model):
    user = snapshot.ForeignKeyField(index=True, model='user')
    class Meta:
        table_name = "attempt"


@snapshot.append
class Question(peewee.Model):
    text = CharField(max_length=1024)
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        table_name = "question"


@snapshot.append
class Audio(peewee.Model):
    attempt = snapshot.ForeignKeyField(index=True, model='attempt')
    question = snapshot.ForeignKeyField(index=True, model='question')
    path = CharField(max_length=25000)
    class Meta:
        table_name = "audio"


@snapshot.append
class Report(peewee.Model):
    attempt = snapshot.ForeignKeyField(index=True, model='attempt')
    phonetic_score = IntegerField()
    grammar_score = IntegerField()
    vocabulary_score = IntegerField()
    coherent_speech_score = IntegerField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        table_name = "report"


def forward(old_orm, new_orm):
    audio = new_orm['audio']
    report = new_orm['report']
    return [
        # Check the field `audio.attempt` does not contain null values
        # Check the field `report.attempt` does not contain null values
    ]


def backward(old_orm, new_orm):
    audio = new_orm['audio']
    return [
        # Apply default value datetime.datetime(2021, 5, 5, 2, 56, 7, 768541) to the field audio.created_at
        audio.update({audio.created_at: datetime.datetime(2021, 5, 5, 2, 56, 7, 768541)}).where(audio.created_at.is_null(True)),
    ]
