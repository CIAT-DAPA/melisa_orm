from mongoengine import Document, StringField, URLField, BooleanField, ListField,EmbeddedDocumentField
from .track import Track
class Melisa(Document):
    """"
    Represents the Melisa in the database.

    Attributes:
    ----------
    name: str
        Name of Melisa. required.
    url_post: str
        Url to return the message. required.
    token: str
        Token or password to validate the melisa. required.
    say_hi: bool
        Indicates if Melisa should say "hi". required.
    say_wait: bool
        Indicates if Melisa should say "wait" when receives a request. required.
    countries: array
        Array with the aclimate's countries id where the melisa is enable. required.

    Methods:
    -------
    save()
        Saves the Melisa object to the database.
    delete()
        Deletes the Melisa object from the database.
    """
    meta = { 'collection': 'melisa'}

    name = StringField(required=True,max_length=50)
    url_post = URLField(required=True)
    token = StringField(required=True,max_length=50)
    say_hi = BooleanField(required=True)
    say_wait = BooleanField(required=True)
    countries = ListField(required=True)
    track = EmbeddedDocumentField(Track, required=True)
