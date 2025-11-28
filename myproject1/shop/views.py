from django.http import HttpResponse

def home(request):
    return HttpResponse("Shop Home Page - Welcome to our store!")

def products(request):
    return HttpResponse("Our Products - Check out our amazing products!")