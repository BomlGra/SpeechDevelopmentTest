from peewee import Model, PostgresqlDatabase

db_conn = PostgresqlDatabase(
    'postgres',
    host='localhost',
    user='postgres',
    port=5432,
    password='postgres',
)


class BaseModel(Model):
    class Meta:
        database = db_conn
    