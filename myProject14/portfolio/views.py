from django.shortcuts import render
from .models import Student

# Create your views here.
def student_list(request):
    students=Student.objects.all()
    # students bhanne chae variable ho jasle chae Students bhanne table ko saaab data lai linxa 

    return render(request, 'portfolio/student_list.html',{'students':students})


# {'students':students})   yo chae context dicitonary ho 
# yesma key and value hunxa 
# first students=key (used in template to access data )


