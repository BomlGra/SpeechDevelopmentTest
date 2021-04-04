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