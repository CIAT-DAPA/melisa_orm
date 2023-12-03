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
from melisa_orm.models.question import Question,QuestionKindEnum,Validation

class TestQuestion(unittest.TestCase):

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

        self.validation = Validation(
            name='name',
            exp='exp',
            error_msg='error_msg',
        )

        self.question = Question(
            form=self.form,
            name='name_question',
            description='description',
            kind=QuestionKindEnum.STRING,
            order=1,
            validations=[(self.validation)],
            track=self.track
            

        )
    def tearDown(self):
        
        self.form.delete()
        self.question.delete()
    def test_create_question(self):

        self.question.save()
        self.assertIsNotNone(self.question.id)


        question = Question.objects(id=self.question.id).first()
        self.assertEqual(question.form, self.form)
        self.assertEqual(question.name,'name_question')
        self.assertEqual(question.description,'description')
        self.assertEqual(question.kind,QuestionKindEnum.STRING)
        self.assertEqual(question.order,1)
        self.assertEqual(question.validations,[(self.validation)])
        self.assertEqual(question.track,question.track)
        



if __name__ == '__main__':
    unittest.main()