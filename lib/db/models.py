import peewee as pw 

from db import DB

class BaseModel(Model):
    class Meta:
        database = DB


class User(BaseModel):
    login = pw.CharField(unique=True)
    user_id = pw.IntegerField(primary_key=True)


class Comment(BaseModel):
    comment_id = pw.IntegerField(primary_key=True)
    user = pw.ForeignKeyField(User, related_name='comments')
    text = pw.CharField()
    created_at = pw.DateField()
    updated_at = pw.DateField()


class Issue(BaseModel):
    issue_id = pw.IntegerField(primary_key=True)


class ActiveIssueCommand(BaseModel):
    comment = pw.ForeignKeyField(Comment)
    issue = pw.ForeignKeyField(Issue)
    chaos_response = pw.ForeignKeyField(Comment)
    seconds_remaining = pw.IntegerField()

    class Meta:
        primary_key = False


class InactiveIssueCommands(BaseModel):
    comment = pw.ForeignKeyField(Comment)

    class Meta:
        primary_key = False
