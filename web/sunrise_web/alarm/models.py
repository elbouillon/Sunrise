from mongoengine import Document, IntField

class Alarm(Document):
    time = IntField(min_value=0, max_value=2359)

