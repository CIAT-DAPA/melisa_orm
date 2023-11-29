import sys
import unittest
import os
import mongomock
from mongoengine import *
from datetime import datetime
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)
from melisaORM.models.thread import Thread,ThreadEnum
from melisaORM.models.track import Track
from melisaORM.models.melisa import Melisa
from melisaORM.models.user import User
from melisaORM.models.intent import Intent, IntentEnum
from melisaORM.models.thread import Thread,ThreadEnum
from melisaORM.models.chat import Chat,ChatKindEnum,ChatStatusEnum,ChatWhomEnum

class Testhread(unittest.TestCase):

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
            name='name_intent',
            group=IntentEnum.QA
        )
        self.intent.save()
        self.thread = Thread(
            user=self.user,
            intent=self.intent,
            status=ThreadEnum.OPENED
        )
        


    def tearDown(self):
        
        self.melisa.delete()
        self.user.delete()
        self.intent.delete()
        self.thread.delete()

    def test_create_action(self):

        self.thread.save()
        self.assertIsNotNone(self.thread.id)


        thread = Thread.objects(id=self.thread.id).first()
        self.assertEqual(thread.user, self.user)
        self.assertEqual(thread.intent, self.intent)
        self.assertEqual(thread.status, ThreadEnum.OPENED)




        

if __name__ == '__main__':
    unittest.main()