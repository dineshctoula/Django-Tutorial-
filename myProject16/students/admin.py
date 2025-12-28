from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # yesle chae admin lai customize gardinxa . heading ma name, age and city dekhauxa 
    list_display = ('name', 'age', 'city')

    search_fields=('name','city')
    # yesle chae search field haldinxa 



    list_filter=('age','city')
    ordering=('name',)
    # ascending or descending order 
    
