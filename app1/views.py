from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


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

#tracking page
#views.py file
def MainPage(request):
    username = request.user.username

    products = Product.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        #print(form.is_valid())
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('tracker')
        else:
            print(form.errors)
    else:
        form = ProductForm()
        #print("hello2")

    context = {
        'username': username,
        'products': products,
        'form': form,
    }

    return render(request,'tracker.html',context)

@login_required
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if product.user == request.user:
        product.delete()
    return redirect('tracker')

def LogOutPage(request):
    logout(request)
    return redirect('home')