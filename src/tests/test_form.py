import sys
import unittest
import os
import mongomock
from mongoengine import *
from datetime import datetime
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)
from melisaORM.models.form import Form
from melisaORM.models.track import Track

class TestForm(unittest.TestCase):

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
    def tearDown(self):
        
        self.form.delete()
    def test_create_form(self):

        self.form.save()
        self.assertIsNotNone(self.form.id)

        print(self.form)

        form = Form.objects(id=self.form.id).first()
        self.assertEqual(form.name, 'name')
        self.assertEqual(form.command, 'comand')

if __name__ == '__main__':
    unittest.main()