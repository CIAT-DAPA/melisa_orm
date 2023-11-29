from .track import Track
from mongoengine import Document, StringField, EmbeddedDocumentField

class Form(Document):
    """"
    Represents a Form in the database.

    Attributes:
    ----------
    name: str
        Melisa where the user registered. required.
    command: str
        Group of the intent. required.

    Methods:
    -------
    save()
        Saves the Intent object to the database.
    delete()
        Deletes the Intent object from the database.
    """
    meta = { 'collection': 'form'}

    name = StringField(required=True)
    command = StringField(required=True)
    track = EmbeddedDocumentField(Track, required=True)