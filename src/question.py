from .form import Form
from .trace import Trace
from mongoengine import Document, ReferenceField, EmbeddedDocument, EmbeddedDocumentListField, StringField, EnumField

class QuestionKindEnum:
    """"
    Represents the type of question
    """
    STRING = 'str'
    IMAGE = 'img'
    NUMBER = 'number'

class Validation(EmbeddedDocument):
    """"
    Represents a validation rule
    """
    name = StringField(required=True)
    exp = StringField(required=True)
    error_msg = StringField(required=True)

class Question(Document):
    """"
    Represents a Question in the database.

    Attributes:
    ----------
    form: ReferenceField
        Form to which it belongs. required
    name: str
        Name of the variable. required
    description: str
        Description of question. required
    kind: QuestionKind
        Type of variable to ask. required.
    order: int
        Set the order to ask the questions to users. required.
    validations: Validation array
        List of validations to do in the question. required.
    track: Track
        Track record. required.

    Methods:
    -------
    save()
        Saves the Intent object to the database
    delete()
        Deletes the Intent object from the database
    """
    meta = { 'collection': 'question'}

    form = ReferenceField(Form)
    name = StringField(required=True)
    description = StringField(required=True)
    kind = EnumField(QuestionKindEnum, required=True)
    order = IntField()
    validations = EmbeddedDocumentListField(Validation, required=True)
    trace = EmbeddedDocumentField(Trace, required=True)