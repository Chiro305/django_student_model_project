from django.db import models

# Create your models here.
class Student(models.Model):
    studentid = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length =50)
    options = (("male","male"),("female","female"))
    gender = models.CharField(choices=options, default="", max_length=20)
    dob = models.DateField(default="")
    photo = models.ImageField(upload_to="images")
    address = models.TextField()
    grades = models.CharField(max_length=2)