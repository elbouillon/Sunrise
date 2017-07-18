from mongoengine import Document, BooleanField, StringField

class Alarm(Document):
    time = StringField(verbose_name='Time',  max_length=5)
    active = BooleanField(default=False, verbose_name='Active')
    day_1 = BooleanField(default=False, verbose_name='MO')
    day_2 = BooleanField(default=False, verbose_name='TU')
    day_3 = BooleanField(default=False, verbose_name='WE')
    day_4 = BooleanField(default=False, verbose_name='TH')
    day_5 = BooleanField(default=False, verbose_name='FR')
    day_6 = BooleanField(default=False, verbose_name='SA')
    day_7 = BooleanField(default=False, verbose_name='SU')

