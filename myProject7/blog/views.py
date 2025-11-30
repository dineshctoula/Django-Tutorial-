from django.shortcuts import render
from datetime import datetime
# Create your views here.

def blog_list(request):
    blogs=[
        {
            "title":"django basic","is_featured":True, "author":"dinesh"
        },

         {
            "title":"django advance","is_featured":False, "author":""
        },



         {
            "title":"django rest","is_featured":False, "author":"Hari"
        },

    ]
    context={
        "blogs":blogs,
        "today":datetime.now(),
        "html_code":"<h1> Welcome to my blog </h1>",
    }
    return render(request,'blog/blog_list.html',context)
