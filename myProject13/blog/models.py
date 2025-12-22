from django.db import models

# Create your models here.
class Student (models. Model):
    name=models.CharField(max_length=50)

    age=models.IntegerField()
    email=models.EmailField(unique=True)

    # email unique hunu paryo 
    # like two studnets can have same email 


    enrollment_date=models.DateField(auto_now_add=True)
    # date is automatically updated when the studetns is first created 


    # pahila makemigrations ane tesh paxe migrate 


    