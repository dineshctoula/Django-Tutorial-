from django.http import HttpResponse

def post_details(request, post_id):
    return HttpResponse(f" <h1>show blog post {post_id}</h1>")



def user_profile(request, username):
     return HttpResponse(f" <h1>profile of user : {username}</h1>")
    

def article_by_year(request,year):
     return HttpResponse(f" <h1> articles from the year: {year}</h1>")
      


def article_details(request, year, month,days):
     
     return HttpResponse(f" <h1> articles from: {year}-{month}-{days}</h1>")