from peewee import *

db = PostgresqlDatabase(
    'postgres',
    host='localhost',
    user='postgres',
    password='postgres',
)

class BaseModel(Model):
    class Meta:
        database = db
