from .form import Form
from .trace import Trace
from mongoengine import Document, ReferenceField, EmbeddedDocument, StringField, EnumField

class ActionRequestEnum:
    """"
    Represents the type of request
    """
    GET = 'get'
    POST = 'post'
    PUT = 'put'

class Action(Document):
    """"
    Represents a Action in the database.

    Attributes:
    ----------
    form: ReferenceField
        Form to which it belongs. required
    name: str
        Name of the action. required
    call_url: str
        Url to send the data. required.
    request: ActionRequestEnum
        Type of request to send data. required.
    track: Track
        Track record. required.


    Methods:
    -------
    save()
        Saves the Intent object to the database.
    delete()
        Deletes the Intent object from the database.
    """
    meta = { 'collection': 'action'}

    form = ReferenceField(Form)
    name = StringField(required=True)
    call_url = StringField(required=True)
    request = EnumField(ActionRequestEnum, required=True)
    trace = EmbeddedDocumentField(Trace, required=True)