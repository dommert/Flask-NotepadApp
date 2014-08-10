# Flask-Netbook Version 0.0.2
# Migration_DB.py
# PeeWee Database Migrations

from peewee import *
from playhouse.migrate import *
from app import app, db

# Database
sql_db = SqliteDatabase('flask_netbook.db')
migrator = SqliteMigrator(sql_db)

# Migration

title_field = CharField(null=True)
#status_field = IntegerField(null=True)

migrate(
    migrator.add_column('Note', 'title', title_field),
    #migrator.add_column('some_table', 'status', status_field),
    #migrator.drop_column('some_table', 'old_column'),
)