from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def HomePage(request):
    return render(request,'index.html')


def SignUpPage(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        uname=fname+" "+lname

        my_user=User.objects.create_user(uname,email,password)
        my_user.save()
        return redirect('login')
        #return HttpResponse("User created successfully")
    return render(request,'signup.html')


def LogInPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        #print(email,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('tracker')
        else:
            return render(request,'login.html',{'error_label': 'Incorrect details!!!'})
    return render(request,'login.html')

def MainPage(request):
    username = request.user.username
    return render(request,'tracker.html',{'username': username})

def LogOutPage(request):
    logout(request)
    return redirect('home')