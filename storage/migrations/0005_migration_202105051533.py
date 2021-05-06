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
class Report(peewee.Model):
    phonetic_score = IntegerField()
    grammar_score = IntegerField()
    vocabular_score = IntegerField()
    coherent_speech_score = IntegerField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        table_name = "report"


@snapshot.append
class Attempt(peewee.Model):
    user = snapshot.ForeignKeyField(index=True, model='user')
    report = snapshot.ForeignKeyField(index=True, model='report', null=True)
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
    attempt = snapshot.ForeignKeyField(backref='audios', index=True, model='attempt')
    question = snapshot.ForeignKeyField(index=True, model='question')
    path = CharField(max_length=25000)
    class Meta:
        table_name = "audio"


def forward(old_orm, new_orm):
    report = new_orm['report']
    return [
        # Apply default value 0 to the field report.vocabular_score
        report.update({report.vocabular_score: 0}).where(report.vocabular_score.is_null(True)),
    ]


def backward(old_orm, new_orm):
    report = new_orm['report']
    return [
        # Apply default value 0 to the field report.vocabulary_score
        report.update({report.vocabulary_score: 0}).where(report.vocabulary_score.is_null(True)),
    ]
