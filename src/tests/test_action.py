import sys
import unittest
import os
import mongomock
from mongoengine import *
from datetime import datetime
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)
from melisa_orm.models.form import Form
from melisa_orm.models.track import Track
from melisa_orm.models.actions import Action, ActionRequestEnum
#
class TestAction(unittest.TestCase):

    def setUp(self):
        disconnect()
        connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)

        self.track = Track(
            user='user',
            created=datetime.now(),
            updated=datetime.now(),
            enable=True
        )
        
        self.form = Form(
            name='name',
            command='comand',
            track=self.track
        )
        self.form.save()

        self.action = Action(
            form=self.form,
            call_url='call url',
            name='name action',
            track=self.track,
            request=ActionRequestEnum.GET 
        )
    def tearDown(self):
        
        self.form.delete()
        self.action.delete()

    def test_create_action(self):

        self.action.save()
        self.assertIsNotNone(self.action.id)

        print(self.action)

        action = Action.objects(id=self.action.id).first()
        self.assertEqual(action.name, 'name action')
        self.assertEqual(action.call_url, 'call url')
        self.assertEqual(action.request, ActionRequestEnum.GET)

if __name__ == '__main__':
    unittest.main()