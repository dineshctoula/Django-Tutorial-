from django.contrib import admin
from .models import Student
from .models import Profile

# Register your models here.
# model lai register garnu parxa admin ma 

admin.site.register(Student)
admin.site.register(Profile)