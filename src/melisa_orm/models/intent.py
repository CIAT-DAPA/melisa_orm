from mongoengine import EmbeddedDocument, StringField, EnumField, IntField
from enum import Enum

class IntentGroupEnum(Enum):
    """"
    Represents the group of intent
    """
    QA = 'qa'
    COMMAND = 'command'
    FORM = 'form'
    UNKONW = 'unknown'

    @staticmethod
    def list():
        return dict((label.name, idx) for idx, label in enumerate(IntentGroupEnum))

class Intent(EmbeddedDocument):
    """"
    Represents an Intent in the database.

    Attributes:
    ----------
    name: str
        Melisa where the user registered. required.
    group: IntentEnum
        Group of the intent. required.
    """

    id = IntField()
    name = StringField(required=True)
    group = EnumField(IntentGroupEnum, required=True)