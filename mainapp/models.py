from django.db import models

# Create your models here.

class UserInfo(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField()
    contact_no=models.CharField(max_length=10)
    age=models.IntegerField()
    problem=models.TextField()



    