import sys
import unittest
import os
import mongomock
from mongoengine import *
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)
from melisa_orm.models.melisa import Melisa
from melisa_orm.models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        disconnect()
        connect('mongoenginetest', host='mongodb://localhost', mongo_client_class=mongomock.MongoClient)
   
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
            user_id='id_user',
            tags={}
        )
        

    def tearDown(self):
        
        self.melisa.delete()
        self.user.delete()

    def test_create_form(self):

        self.user.save()
        self.assertIsNotNone(self.user.id)


        user = User.objects(id=self.user.id).first()
        self.assertEqual(user.melisa, self.melisa)
        self.assertEqual(user.user_id, 'id_user')
        self.assertEqual(user.tags, {})
       
        


if __name__ == '__main__':
    unittest.main()