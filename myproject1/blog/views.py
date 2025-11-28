from django.http import HttpResponse

def home(request):
    return HttpResponse("Blog Home Page - Welcome to our blog!")

def about(request):
    return HttpResponse("About Our Blog - Learn more about us!")