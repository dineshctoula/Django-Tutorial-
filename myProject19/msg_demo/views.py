from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def show_msg(request):
    messages.debug(request, 'This is a debug message')
    messages.info(request,'This is an info message')
    messages.success(request,'This is an success message')
    messages.warning(request,'This is an warning message')
    messages.error(request,'This is an error message')







    return render(request,'message.html')
