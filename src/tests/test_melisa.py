import sys
import unittest
import os
import mongomock
from mongoengine import *
dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)
from melisa_orm.models.melisa import Melisa


class TestMelisa(unittest.TestCase):

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
    def tearDown(self):
        
        self.melisa.delete()

    def test_create_form(self):

        self.melisa.save()
        self.assertIsNotNone(self.melisa.id)


        melisa = Melisa.objects(id=self.melisa.id).first()
        self.assertEqual(melisa.name, 'melissa_name')
        self.assertEqual(melisa.url_post, 'https://www.ejemplo.com')
        self.assertEqual(melisa.token, '57eueheh')
        self.assertEqual(melisa.say_hi, True)
        self.assertEqual(melisa.say_wait, True)
        self.assertEqual(melisa.countries, ['colombia','panama'])
        


if __name__ == '__main__':
    unittest.main()