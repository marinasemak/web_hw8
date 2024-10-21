from mongoengine import BooleanField, Document, StringField, connect

connect(db="contacts", host="mongodb://mongo.user:secret_pass@localhost/")


class Contact(Document):
    fullname = StringField(max_length=120, required=True)
    email = StringField(max_length=120, required=True)
    is_sent = BooleanField(default=False)
