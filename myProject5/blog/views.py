from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self, name, age):
        self.name = name #self.name ley chae store the name of object that can be accessed while typing user.name 
        self.age = age
        # def bhanney chae constructor ho jun automatically ru hunxa when user object is created



def home(request):
    context = {  #context bhaneko chae dictionay ho jasle chae template ma pathauney data lai store garxa
        "name": "dinesh sitoula",
        "age": 25,
        "skills": ["python", "django", "flask"], # yo braket ko bhaneko chae list ho 
        "user": User("hari", 30),
        "blog": {   #yo bhaneko chae nested dictionary ho 
            "title": "django template intro",
            "content": "<br> this is bold </b>",
            "created_at": datetime(2025, 8, 18, 10, 30)
        },
        "empty_value": None,
    }
    return render(request, "blog/home.html", context) 
