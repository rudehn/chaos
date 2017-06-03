from peewee import SqliteDatabase
from settings import DB_CONFIG
from .models import User, Comment, InactiveIssueCommands
from .models import Issue, ActiveIssueCommand


import logging

__log = logging.getLogger("db")

DB = SqliteDatabase(DB_CONFIG["filename"])

try:
	DB.connect()
	DB.create_tables([User, Comment, Issue,
					  ActiveIssueCommand,
					  InactiveIssueCommands], safe=True)
	DB.close()
except Exception as e:
	__log.exception("Something went wrong with the db")
	raise e