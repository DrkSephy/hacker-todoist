from django.db import models
from mongoengine import *

class Entries(Document):
    due = StringField(required=True)
    title = StringField(required=True)
    username = StringField(required=True)

