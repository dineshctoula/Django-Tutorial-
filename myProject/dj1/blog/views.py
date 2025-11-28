from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("welcome to the blog home page!")


from django.http import HttpResponse

def about(request):
    a = 10 + 50
    return HttpResponse(f"About page: {a}")