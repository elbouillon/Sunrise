from mongoengine import Document, IntField,  BooleanField

class Alarm(Document):
    time = IntField(min_value=0, max_value=2359)
    active = BooleanField(default=False)

