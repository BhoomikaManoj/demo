from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth
from AMSapp.models import leave
# User, auth, authenticate, login
from AMSapp.models import Newuser
from django.contrib import messages
from AMSapp.models import Mymodel,worktime

# Create your views here.
def homepage(request):
    return render(request,'AMSapp/home.html')

def register(request):
    if request.method == 'POST':
        if(request.POST.get('employeeName') and request.POST.get('username') and request.POST.get('password') and request.POST.get('password1') and request.POST.get('emailId') and request.POST.get('phoneNo')):
            saverecord=Mymodel()
            saverecord.employeeName=request.POST.get('employeeName')
            saverecord.username=request.POST.get('username')
            saverecord.password=request.POST.get('password')
            saverecord.emailId=request.POST.get('emailId')
            saverecord.phoneNo=request.POST.get('phoneNo')
            saverecord.save()
            messages.success(request,"new user registration details saved successsfully")
            return render(request,"AMSapp/home.html")
    else:
        return render(request,'AMSapp/register.html')

# def loginpage(request):
#     if request.method== 'POST':
#         username = request.POST.get('username')
#         password = request.post.get('password')

#         if username and password:
#             user = auth.authenticate(username=username,password=password)

#             if user is not None:
#                 login(request,user)
#                 return redirect("/")
#             else:
#                 messages.error(request,'invaild credentials')
#                 return redirect('login')
#         else:
#             messages.error(request,'Fill out all fields')
#     return render(request,'AMSapp/login.html')

def loginpage(request):
    if request.method=="POST":
        try:
            Userdetails=Newuser.objects.get(username=request.POST['username'],password=request.POST['password'])
            print("username",Userdetails)
            request.session['username']=Userdetails.username
            return render(request,'AMSapp/home.html')
        except Newuser.DoesNotExist as e:
            messages.success(request,'username /password invaild..!')
    return render(request,'AMSapp/login.html')

# def logout(request):
#     try:
#         del request.session['emailId']
#     except:
#         return render(request,'AMSapp/home.html')
#     return render(request,'AMSapp/home.html')

def leavepage(request):
    if request.method == 'POST':
        if (request.POST.get('employeeName') and request.POST.get('StartDate') and request.POST.get('EndDate') and request.POST.get('LeaveDay')):
            saverecord=leave()
            saverecord.employeeName=request.POST.get('employeeName')
            saverecord.StartDate=request.POST.get('StartDate')
            saverecord.EndDate=request.POST.get('EndDate')
            saverecord.LeaveDay=request.POST.get('LeaveDay')
            saverecord.save()
            messages.success(request,"Apply Leave successsfully")
            return render(request,"AMSapp/leave.html")
    else:
        return render(request,'AMSapp/leave.html')

def worktimepage(request):
    if request.method == 'POST':
        if (request.POST.get('employeeName') and request.POST.get('clockIn') and request.POST.get('clockOut')):
            saverecord=worktime()
            saverecord.employeeName=request.POST.get('employeeName')
            saverecord.clockIn=request.POST.get('clockIn')
            saverecord.clockOut=request.POST.get('clockOut')
            saverecord.save()
            return render(request,"AMSapp/worktime.html")
    else:
        return render(request,'AMSapp/worktime.html')
