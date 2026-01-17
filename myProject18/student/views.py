from django.shortcuts import render
from .forms import StudentForm


# Create your views here.
def student_create(request):
    form=StudentForm()
    # jaba user ley form khulxa tyo bela empty hunxa where no daya is submitted 

    if request.method=='POST':
        form=StudentForm(request.POST)
        # when user submits the form. ho yo ane request.POST ma chae name, age, email hunxa 
        if form.is_valid():
            form.save()
            return render(request,'student_success.html')
    return render (request,'student_form.html',{'form':form})
# yedi form valid bhayena bhane or form chae get request ho bhane  mathi ko dekhaune
#   render(request, template_name, context) yo chae syntaxa ho

# {'form': form}
# Means:

# Key → 'form' (name used in HTML)

# Value → form (StudentForm object)