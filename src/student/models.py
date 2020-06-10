from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=120)
    student_class = models.CharField(max_length=120, null=True, blank=True)
    student_grade = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.name)


    