from django.test import TestCase
from .models import student
# Create your tests here.

class TestStudentDB(TestCase):
    def setUp(self):
        self.stu = student.objects.create(name='abc', student_class='somepasS23', student_grade='B')
    def test_student_created(self):
        stu =  student.objects.get(name='abc')
        self.assertEqual(stu.name, 'abc')
        self.assertEqual(stu.student_class, 'somepasS23')

    def test_student_deleted(self):
        stu =  student.objects.get(name='abc')
        stu.delete()
        print("********************")
        try:
            stu = stu.objects.get(username="abc")
        except:
            stu =  None
        
        print(stu)
        self.assertNotEqual(stu, "abc")