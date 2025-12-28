from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
# Create your views here.


def contact_form(request):
    return render( request,'contact.html')




def submit_contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        message=request.POST.get('message')



        if name and message:
            # name ane message khali hunu hudaenah 
            Contact.objects.create(name=name, message=message)
            # yesle chae haleko data lai database ms save garne raixa 
            return HttpResponse (f" Thank you, {name}, for your message !")
        else:
            return HttpResponse("Please provide both name and message")
    return redirect('contact_form')
# yo conotact_formm chae chalxa when request is not post 