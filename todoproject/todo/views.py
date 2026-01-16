from django.shortcuts import render,redirect, get_object_or_404

# get_object_or_404_ ley chae database bata object lai fetch garxa ane bhetene bhane 404 error page bhandinxa 

# import reverse url lee chae url name lai actual url ma convert gardina ane it is used for dynamic redirects



from django.urls import reverse
from .models import Task
# Create your views here.
def task_list(request):
    task=Task.objects.all().order_by('-created_at')
    return render(request, 'todo/task_list.html',{'tasks':task})
        #    yesma tasks bhaneko chae template ma use hune ho 
        #task= chae actual data from database 

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()  # fixed typo

        if title:
            Task.objects.create(title=title, description=description)
            return redirect(reverse('todo:task_list'))
        
        error = "Title cannot be empty."
        return render(request, 'todo/task_form.html', {'error': error})
    
    return render(request, 'todo/task_form.html')






def task_update(request, pk):
    # Fetch task or show 404 if not found
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        completed = request.POST.get('completed') == 'on'  # checkbox

        if title:
            # Update task
            task.title = title
            task.description = description
            task.completed = completed
            task.save()  # save changes to database

            # Redirect to task list
            return redirect(reverse('todo:task_list'))
        
        # If title empty, show form with error
        return render(request, 'todo/task_form.html', {'task': task, 'error': "Title cannot be empty."})
    
    # GET request: show form with current task data
    return render(request, 'todo/task_form.html', {'task': task})




def task_delete(request, pk):
    task=get_object_or_404(Task, pk=pk)
    if request.method=='POST':
        task.delete()
        return redirect(reverse('todo:task_list'))
    return render(request,'todo/task_confirm_delete.html',{'task':task})





def task_toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
    return redirect('todo:task_list')

