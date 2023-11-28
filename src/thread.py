from .user import User
from .intent import Intent
from mongoengine import Document, EnumField

class ThreadEnum:
    """"
    Represents the status of thread
    """
    OPENED = 'opened'
    CLOSED = 'closed'

class Thread(Document):
    """"
    Represents a thread of chat with a user in the database.

    Attributes:
    ----------
    user: ReferenceField
        Melisa where the user registered. required.
    intent: ReferenceField
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
    intent = ReferenceField(Intent)
    status = EnumField(ThreadEnum, required=True)
