from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from studentapp.models import studentmodel

def home(request):
    return render(request,'home.html')

# Create your views here.
def register(request):
    if request.method == 'POST':
        if(request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('currentjob') and request.POST.get('location')):
            saverecord=studentmodel()
            saverecord.firstname=request.POST.get('firstname')
            saverecord.lastname=request.POST.get('lastname')
            saverecord.currentjob=request.POST.get('currentjob')
            saverecord.location=request.POST.get('location')

            saverecord.save()
            messages.success(request,"new user registration details saved successsfully")
            return render(request,'home.html')
    else:
        return render(request,'register.html')


    # if request.method == 'POST':
    #     firstname=request.POST.get('firstname')
    #     lastname=request.POST.get('lastname')
    #     currentjob=request.POST.get('currentjob')
    #     location=request.POST.get('location')
    #     user = User.objects.create_user(firstname = firstname, lastname = lastname, currentjob = currentjob, location = location)
    #     user.save();
    #     print('user created')
    #     return render(request,'register.html')
    # else:
    #     return render(request,'register.html')
    
