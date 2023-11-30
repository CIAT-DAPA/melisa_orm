from .thread import Thread
from mongoengine import Document, DateTimeField, StringField, DictField, EnumField, ListField, ReferenceField
from enum import Enum

class ChatStatusEnum(Enum):
    """"
    Representa el estado del chat
    """
    OK = 'ok'
    ERROR = 'error'

class ChatWhomEnum(Enum):
    """"
    Representa quién escribe el mensaje
    """
    USER = 'user'
    SYSTEM = 'system'

class ChatKindEnum(Enum):
    """"
    Representa el tipo de entrada
    """
    TEXT = 'text'
    IMAGE = 'img'

class Chat(Document):
    """"
    Representa un chat en la base de datos.

    Atributos:
    ----------
    thread: ReferenceField
        Hilo del chat. requerido.
    date: datetime
        Fecha del mensaje recibido. requerido.
    original: str
        Texto original recibido del mensaje. requerido.
    text: str
        Texto limpio recibido del mensaje. requerido.
    slot: str

    Métodos:
    -------
    save()
        Guarda el objeto Chat en la base de datos.
    delete()
        Elimina el objeto Chat de la base de datos.
    """
    meta = { 'collection': 'chat'}

    thread = ReferenceField(Thread, required=True)
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
