from django.urls import path
from .import views

app_name='todo'
# namespace bata leko 

urlpatterns=[
    path('',views.task_list, name='task_list'),

    path('add/',views.task_create, name='task_create'),

    path('edit/<int:pk>/',views.
         task_update, name='task_update'),
        #  pk bhaneko chae url parameter ho.. yeslae primary key bhaninxa 



     path('delete/<int:pk>/',views.task_delete, name='task_delete'),




     path('toggle/<int:pk>/',views.task_toggle_complete, name='task_toggle_complete'),


   
]

