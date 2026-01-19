from django.shortcuts import render,get_object_or_404,redirect
from .forms import StudentForm
from .models import Student


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




def student_list(request):
    students=Student.objects.all()
    # students bhanne variable ho ra yesle chae Student bhanne table bata sabai data uthauxa
    return render(request,'student_list.html',{'students':students})




def student_detail(request,pk):
    student=get_object_or_404(Student, pk=pk)
    return render(request,'student_detail.html',{'student':student})




def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    # yedi student exist gardaina bhane 404 error aaucha

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        # request.POST = updated data
        # instance=student = existing student update gar

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        # GET request ma form lai existing data sanga load gar
        form = StudentForm(instance=student)

    return render(request, 'student_form.html', {'form': form})
