from mongoengine import Document, IntField, BooleanField, ListField

class Alarm(Document):
    time = IntField(min_value=0, max_value=2359, verbose_name='Time')
    active = BooleanField(default=False)
    weekday_1 = BooleanField(default=False, verbose_name='MO')
    weekday_2 = BooleanField(default=False, verbose_name='TU')
    weekday_3 = BooleanField(default=False, verbose_name='WE')
    weekday_4 = BooleanField(default=False, verbose_name='TH')
    weekday_5 = BooleanField(default=False, verbose_name='FR')
    weekday_6 = BooleanField(default=False, verbose_name='SA')
    weekday_7 = BooleanField(default=False, verbose_name='SU')

