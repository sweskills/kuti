import unittest
from app.models import Teacher, School


class TeacherModelTest(unittest.TestCase):
    def test_password_setter(self):
        u = Teacher(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = Teacher(password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = Teacher(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salt_are_random(self):
        u = Teacher(password='cat')
        u2 = Teacher(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)

class SchoolModeltest(unittest.TestCase):
    def test_password_setter(self):
        u = School(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = School(password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = School(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salt_are_random(self):
        u = School(password='cat')
        u2 = School(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)
