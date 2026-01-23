from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
# Create your views here.


def register_view(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            # yesle chae auto login gardinxa
            messages.success(request,'Registration successful. You can now logged in. ')
            return redirect('dashboard')
        else:
            messages.error(request,'Registration failed')
    else:
        form=RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})







def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        # yesle chae autheticate garxa
        if user is not None:   #yedi login details correct xa bhane

            login(request,user)  #login successful
            messages.success(request,'Login Successful')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Username and Password')
    return render (request,'accounts/login.html')





def logout_view(request):
    logout(request)
    messages.success(request, 'You Have Been logged out Successfully')
    return redirect('login')







def dashboard_view(request):
    return render (request,'accounts/dashboard.html')


