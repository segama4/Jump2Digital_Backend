from mongoengine import Document, StringField, FloatField


class Skin(Document):
    name = StringField(required=True)
    type = StringField()
    price = FloatField(required=True)
    color = StringField()
