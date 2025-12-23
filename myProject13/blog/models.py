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

    city=models.CharField(max_length=100, default='Unknown')
    # pahila makemigrations ane tesh paxe migrate 
    def __str__(self):
        return self.name
    # human readable output dinxa so def str lekheko 
    # student ko name ko hisab ley object dekhauxa so. 

    






    