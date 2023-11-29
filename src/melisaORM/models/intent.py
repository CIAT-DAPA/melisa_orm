from mongoengine import Document, StringField, EnumField
from enum import Enum

class IntentEnum(Enum):
    """"
    Represents the group of intent
    """
    QA = 'qa'
    COMMAND = 'command'
    FORM = 'form'

class Intent(Document):
    """"
    Represents an Intent in the database.

    Attributes:
    ----------
    name: str
        Melisa where the user registered. required.
    group: IntentEnum
        Group of the intent. required.

    Methods:
    -------
    save()
        Saves the Intent object to the database.
    delete()
        Deletes the Intent object from the database.
    """
    meta = { 'collection': 'intent'}

    name = StringField(required=True)
    group = EnumField(IntentEnum, required=True)