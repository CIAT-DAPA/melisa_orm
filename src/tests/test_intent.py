import sys
import unittest
import os
import mongomock
from mongoengine import *
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)
from melisa_orm.models.intent import Intent,IntentGroupEnum


class TestIntent(unittest.TestCase):

    def setUp(self):
        disconnect()
        connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)
   
        self.intent = Intent(
            name='name_intent',
            group=IntentGroupEnum.QA,
            ext_id=1
        )
    def tearDown(self):
        
        self.intent.delete()

    def test_create_form(self):

        self.intent.save()
        self.assertIsNotNone(self.intent.id)


        intent = Intent.objects(id=self.intent.id).first()
        self.assertEqual(intent.name, 'name_intent')
        self.assertEqual(intent.group, IntentGroupEnum.QA)
        self.assertEqual(intent.ext_id, 1)

if __name__ == '__main__':
    unittest.main()