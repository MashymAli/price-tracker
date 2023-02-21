from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
import requests
from bs4 import BeautifulSoup as bs



# Create your views here.
def HomePage(request):
    return render(request,'index.html')


def SignUpPage(request):
    if request.method=='POST':
        uname=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        # Check if user with the same username already exists
        if User.objects.filter(username=uname).exists():
            error_message = 'Username already exists!.'
            return render(request, 'signup.html', {'error_message': error_message})
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            error_message2 = 'Email already exists!'
            return render(request, 'signup.html', {'error_message2': error_message2})

        my_user=User.objects.create_user(uname,email,password)
        my_user.save()
        return redirect('login')
        #return HttpResponse("User created successfully")
    return render(request,'signup.html')


def LogInPage(request):
    if request.method=='POST':
        username=request.POST.get('name')
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
    
    # Check if user has already submitted a product
    has_product = Product.objects.filter(user=request.user).exists()
    error_msg = ""

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if has_product:
            # If there is already a product, display an error message
            error_msg = 'You can only track one product at a time. Please delete the existing product before adding a new one.'
        else:
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Connection': 'keep-alive'
                }
            
                page=requests.get(product.url,headers=headers)
                #print(page.content)
                soup = bs(page.content,"html.parser")
                
                try:
                    product_name = soup.find('span', attrs={'class': 'a-size-large'}).get_text().strip()
                    product_name = product_name.split(',')[0].strip()
                except:
                    product_name = "Product 1"

                product.name=product_name
                
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
        'error_msg': error_msg,
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