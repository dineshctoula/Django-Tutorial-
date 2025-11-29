from django.shortcuts import render
from datetime import datetime

# Create your views here.

def blog_details(request):
    post={
        "title": "my second templates post",
        "description":"django is high level lenguage",
        "author":None,
        "created_at":datetime(2025,9,19,20,1),
        "comments_count":5,
        "tags":["django","python","web"],

        "price":100,
        "number":7,
        # yo mathi ko chae dictiooinary ho jun chae templates ma pass hunxa 

    }
    return render(request,'blog/blog_details.html', {"post":post})