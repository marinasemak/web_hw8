from mongoengine import (
    connect,
    Document,
    StringField,
    DateField,
    ReferenceField,
    ListField,
    CASCADE,
)
from datetime import datetime


class Author(Document):
    fullname = StringField(required=True, max_length=50, unique=True)
    born_date = DateField()
    born_location = StringField(max_length=150)
    description = StringField()

    meta = {"collection": "authors"}


class Quote(Document):
    tags = ListField()
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()

    meta = {"collection": "quotes"}
