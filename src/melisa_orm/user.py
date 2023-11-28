from .melisa import Melisa
from mongoengine import Document, StringField, ReferenceField, DictField

class User(Document):
    """"
    Represents a User in the database.

    Attributes:
    ----------
    melisa: ReferenceField
        Melisa where the user registered. required.
    user_id: str
        Id of the user in the Melisa. required.
    tags: DictField
        Extra information of the user required by the Melisa. required.

    Methods:
    -------
    save()
        Saves the User object to the database.
    delete()
        Deletes the User object from the database.
    """
    meta = { 'collection': 'user'}

    melisa = ReferenceField(Melisa)
    user_id = StringField(required=True)
    tags = DictField()