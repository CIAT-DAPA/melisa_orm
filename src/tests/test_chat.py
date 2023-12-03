import sys
import unittest
import os
import mongomock
from mongoengine import *
from datetime import datetime
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)
from melisa_orm.models.track import Track
from melisa_orm.models.melisa import Melisa
from melisa_orm.models.user import User
from melisa_orm.models.intent import Intent, IntentGroupEnum
from melisa_orm.models.thread import Thread,ThreadEnum
from melisa_orm.models.chat import Chat,ChatKindEnum,ChatStatusEnum,ChatWhomEnum

class TestChat(unittest.TestCase):

    def setUp(self):
        disconnect()
        connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)

        self.track = Track(
            user='user',
            created=datetime.now(),
            updated=datetime.now(),
            enable=True
        )

        self.melisa = Melisa(
            name='melissa_name',
            url_post='https://www.ejemplo.com',
            token='57eueheh',
            say_hi=True,
            say_wait=True,
            countries=['colombia','panama']
        )
        self.melisa.save()

        self.user = User(
            melisa=self.melisa,
            user_id='https://www.ejemplo.com',
            tags={}
        )
        self.user.save()

        self.intent = Intent(
            id=1,
            name='name_intent',
            group=IntentGroupEnum.QA
        )
        self.thread = Thread(
            user=self.user,
            intent=self.intent,
            status=ThreadEnum.OPENED
        )
        self.thread.save()

        self.chat = Chat(
            thread=self.thread,
            date=datetime(2023, 1, 1, 12, 0, 0),
            original='original',
            text='text',
            slots={},
            tags={},
            ext_id='ext-id',
            status=ChatStatusEnum.OK,
            whom=ChatWhomEnum.USER,
            kind_msg=ChatKindEnum.TEXT
        )

    def tearDown(self):

        self.melisa.delete()
        self.user.delete()
        self.thread.delete()
        self.chat.delete()

    def test_create_chat(self):

        self.chat.save()
        self.assertIsNotNone(self.chat.id)

        print(self.chat)

        chat = Chat.objects(id=self.chat.id).first()
        self.assertEqual(chat.thread, self.thread)
        self.assertEqual(chat.original, 'original')
        self.assertEqual(chat.date, datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(chat.text, 'text')
        self.assertEqual(chat.slots, {})
        self.assertEqual(chat.tags, {})
        self.assertEqual(chat.ext_id, 'ext-id')
        self.assertEqual(chat.status, ChatStatusEnum.OK)
        self.assertEqual(chat.whom, ChatWhomEnum.USER)
        self.assertEqual(chat.kind_msg, ChatKindEnum.TEXT)



if __name__ == '__main__':
    unittest.main()