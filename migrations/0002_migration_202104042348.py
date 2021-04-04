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
class Report(peewee.Model):
    user = snapshot.ForeignKeyField(backref='reports', index=True, model='user')
    date = DateField(default=datetime.datetime(2021, 4, 4, 23, 48, 33, 335947))
    score = IntegerField()
    class Meta:
        table_name = "report"


