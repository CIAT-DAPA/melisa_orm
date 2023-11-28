from mongoengine import Document, EmbeddedDocument, DateTimeField, StringField, BooleanField

class Track(EmbeddedDocument):
    """"
    Represents a class to trace the changes in the records

    Attributes:
    ----------
    user: str
        User who execute the last change. required
    created: datetime
        Date when the record was created. required
    updated: datetime
        Date when the record was updated. required
    enable: bool
        Set if the record is enable or disable. required.
    """
    user = StringField(required=True)
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)
    enable = BooleanField()
