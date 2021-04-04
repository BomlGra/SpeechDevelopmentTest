# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class User(peewee.Model):
    email = CharField(max_length=128)
    password = CharField(max_length=128)
    name = CharField(max_length=128)
    age = IntegerField()
    class Meta:
        table_name = "user"


@snapshot.append
class Audio(peewee.Model):
    user = snapshot.ForeignKeyField(backref='audio', index=True, model='user')
    path = CharField(max_length=256)
    class Meta:
        table_name = "audio"


@snapshot.append
class Question(peewee.Model):
    text = CharField(max_length=256)
    answer = snapshot.ForeignKeyField(index=True, model='audio')
    class Meta:
        table_name = "question"


@snapshot.append
class Report(peewee.Model):
    user = snapshot.ForeignKeyField(backref='reports', index=True, model='user')
    date = DateField(default=datetime.datetime(2021, 4, 5, 0, 27, 56, 929626))
    score = IntegerField()
    class Meta:
        table_name = "report"


def forward(old_orm, new_orm):
    audio = new_orm['audio']
    return [
        # Apply default value '' to the field audio.path
        audio.update({audio.path: ''}).where(audio.path.is_null(True)),
    ]


def backward(old_orm, new_orm):
    audio = new_orm['audio']
    return [
        # Apply default value '' to the field audio.link
        audio.update({audio.link: ''}).where(audio.link.is_null(True)),
    ]
