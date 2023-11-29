# ORM MELISA

![GitHub release (latest by date)](https://img.shields.io/github/v/release/CIAT-DAPA/melisa_orm) ![](https://img.shields.io/github/v/tag/CIAT-DAPA/melisa_orm)

## Features

- Built using Mongoengine for MongoDB
- Supports Python 3.x

## Getting Started

To use this Models, it is necessary to have an instance of MongoDB running.

### Prerequisites

- Python 3.x
- MongoDB

## Usage

This ORM can be used as a library in other Python projects. The models are located in the my_orm/models folder, and can be imported like any other Python module. To install this orm as a library you need to execute the following command:

````bash
pip install git+https://github.com/CIAT-DAPA/melisa_orm
````

If you want to download a specific version of orm you can do so by indicating the version tag (@v0.0.0) at the end of the install command 

````bash
pip install git+https://github.com/CIAT-DAPA/melisa_orm@v0.2.0
````

## Models

### Action

Represents a Action in the database.

Attributes:

- form: `ObjectId` Reference to Form.
- name: `str` name of the action.
- call_url: `str` call url.
- request: `enum`  restrict the values of the request field.
- track: `class`  class that handles traceability.

name = StringField(required=True)
    call_url = StringField(required=True)
    request = EnumField(ActionRequestEnum, required=True)
    track = EmbeddedDocumentField(Track, required=True)


### Chat

Represents a chat entry in the database.

Attributes:

- thread: `ReferenceField` Reference to Thread. Required.
- date: `datetime` Date of the received message. Required.
- original: `str` Original text received from the message. Required.
- text: `str` Cleaned text received from the message. Required.
- slots: `dict` Dictionary for storing slots.
- tags: `dict` Dictionary for storing tags.
- ext_id: `str` External ID with a maximum length of 200 characters.
- status: `enum` Represents the status of the chat. Required. [ChatStatusEnum](#chatstatusenum)
- whom: `enum` Represents who wrote the message. Required. [ChatWhomEnum](#chatwhomenum)
- values: `list` List for storing values.
- kind_msg: `enum` Represents the type of message. Required. [ChatKindEnum](#chatkindenum)

Methods:

- `save()`: Saves the Chat object to the database.
- `delete()`: Deletes the Chat object from the database.

Enums:

#### ChatStatusEnum
Represents the status of the chat.

- OK: 'ok'
- ERROR: 'error'

#### ChatWhomEnum
Represents who wrote the message.

- USER: 'user'
- SYSTEM: 'system'

#### ChatKindEnum
Represents the type of entry.

- TEXT: 'text'
- IMAGE: 'img'

### Form

Represents a form in the database.

Attributes:

- name: `str` Name of the Melisa where the user registered. Required.
- command: `str` Group of the intent. Required.
- track: `class` Class that handles traceability. Required. [Track](#track)

Methods:

- `save()`: Saves the Form object to the database.
- `delete()`: Deletes the Form object from the database.

Embedded Class:

#### Track
Class that handles traceability.

- `user`: `str` User associated with the track.
- `created`: `datetime` Date and time of creation.
- `updated`: `datetime` Date and time of the last update.
- `enable`: `bool` Indicates if the track is enable

### Intent

Represents an intent in the database.

Attributes:

- name: `str` Name of the Melisa where the user registered. Required.
- group: `enum` Group of the intent. Required. [IntentEnum](#intentenum)

Methods:

- `save()`: Saves the Intent object to the database.
- `delete()`: Deletes the Intent object from the database.

Enums:

#### IntentEnum
Represents the group of intent.

- QA: 'qa'
- COMMAND: 'command'
- FORM: 'form'

### Melisa

Represents the Melisa in the database.

Attributes:

- name: `str` Name of Melisa. Required. Limited to a maximum length of 50 characters.
- url_post: `str` URL to return the message. Required.
- token: `str` Token or password to validate the melisa. Required. Limited to a maximum length of 50 characters.
- say_hi: `bool` Indicates if Melisa should say "hi". Required.
- say_wait: `bool` Indicates if Melisa should say "wait" when receiving a request. Required.
- countries: `array` Array with the aclimate's countries ID where the melisa is enabled. Required.

Methods:

- `save()`: Saves the Melisa object to the database.
- `delete()`: Deletes the Melisa object from the database.


### Question

Represents a Question in the database.

Attributes:

- form: `ReferenceField` Form to which it belongs. Required.
- name: `str` Name of the variable. Required.
- description: `str` Description of the question. Required.
- kind: `enum` Type of variable to ask. Required. [QuestionKindEnum](#questionkindenum)
- order: `int` Set the order to ask the questions to users. Optional.
- validations: `array` List of validations to apply to the question. Required. [Validation](#validation)
- track: `class` Track record. Required. [Track](#track)

Methods:

- `save()`: Saves the Question object to the database.
- `delete()`: Deletes the Question object from the database.

Enums:

#### QuestionKindEnum
Represents the type of question.

- STRING: 'str'
- IMAGE: 'img'
- NUMBER: 'number'

Embedded Class:

#### Validation
Represents a validation rule.

- `name`: `str` Name of the validation rule. Required.
- `exp`: `str` Expression or rule to validate. Required.
- `error_msg`: `str` Error message to display on validation failure. Required.

#### Track
Class that handles traceab


### Thread

Represents a thread of chat with a user in the database.

Attributes:

- user: `ReferenceField` Melisa where the user registered. Required.
- intent: `ReferenceField` Intent discovered. Required.
- status: `enum` Status of the current thread. Required. [ThreadEnum](#threadenum)

Methods:

- `save()`: Saves the Thread object to the database.
- `delete()`: Deletes the Thread object from the database.

Enums:

#### ThreadEnum
Represents the status of the thread.

- OPENED: 'opened'
- CLOSED: 'closed'


### User

Represents a User in the database.

Attributes:

- melisa: `ReferenceField` Melisa where the user registered. Required.
- user_id: `str` ID of the user in the Melisa. Required.
- tags: `DictField` Extra information of the user required by the Melisa. Optional.

Methods:

- `save()`: Saves the User object to the database.
- `delete()`: Deletes the User object from the database.

