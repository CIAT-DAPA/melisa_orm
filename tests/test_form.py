import unittest
from mongoengine import connect, disconnect
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
orm_dir_path = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.append(orm_dir_path)

from src.form import Form
from datetime import datetime

class TestForm(unittest.TestCase):

    def setUp(self):
        disconnect()
        # Connect with the database
        connect('test_melisa', host='mongomock://localhost')
        self.now = datetime.now()
        self.form = Form(
            name='Test form',
            command='test',
            trace=Trace(user = "user", created = self.now, updated = self.now, enabled = True)
        )

    def test_create_form(self):
        # Crea un nuevo adm1
        self.form.save()
        self.assertIsNotNone(self.form.id)

        # Verifica que el adm1 haya sido creado exitosamente
        form1 = Form.objects(id=self.form.id).first()
        self.assertEqual(form1.name, 'Test form')
        self.assertEqual(form1.command, 'test')

if __name__ == '__main__':
    unittest.main()