from .thread import Thread
from mongoengine import Document, DateTimeField, StringField, DictField, EnumField, ListField

class ChatStatusEnum:
    """"
    Represents the status of the chat
    """
    OK = 'ok'
    ERROR = 'error'

class ChatWhomEnum:
    """"
    Represents whom writes the message
    """
    USER = 'user'
    SYSTEM = 'system'

class ChatKindEnum:
    """"
    Represents the type of input
    """
    TEXT = 'text'
    IMAGE = 'img'

class Chat(Document):
    """"
    Represents a Form in the database.

    Attributes:
    ----------
    thread: ReferenceField
        Thread of the chat. required.
    date: datetime
        Date of received message. required.
    original: str
        Original text received from message. required.
    text: str
        Text clean received from message. required.
    slot: str


    Methods:
    -------
    save()
        Saves the Chat object to the database.
    delete()
        Deletes the Chat object from the database.
    """
    meta = { 'collection': 'chat'}

    thread = ReferenceField(Thread)
    date = DateTimeField(required=True)
    original = StringField(required=True)
    text = StringField(required=True)
    slots = DictField()
    tags = DictField()
    ext_id = StringField(max_length=200)
    status = EnumField(ChatStatusEnum, required=True)
    whom = EnumField(ChatWhomEnum, required=True)
    values = ListField()
    kind_msg = EnumField(ChatKindEnum, required=True)