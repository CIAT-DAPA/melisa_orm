from .user import User
from .intent import Intent
from mongoengine import Document, EnumField,ReferenceField,EmbeddedDocumentField
from enum import Enum

class ThreadEnum(Enum):
    """"
    Represents the status of thread
    """
    OPENED = 'opened'
    CLOSED = 'closed'

class IntentGroupEnum(Enum):
    """"
    Represents the group of intent
    """
    QA = 'qa'
    COMMAND = 'command'
    FORM = 'form'

class Thread(Document):
    """"
    Represents a thread of chat with a user in the database.

    Attributes:
    ----------
    user: ReferenceField
        Melisa where the user registered. required.
    intent: EmbeddedDocumentField
        Intent discovered. required.
    status: ThreadEnum
        Status of the current thread. required.

    Methods:
    -------
    save()
        Saves the User object to the database.
    delete()
        Deletes the User object from the database.
    """
    user = ReferenceField(User)
    intent = EmbeddedDocumentField(Intent, required=True)
    status = EnumField(ThreadEnum, required=True)
