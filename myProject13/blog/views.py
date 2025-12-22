

# Create your views here.
from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog.html')