from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from .models import User
from django.contrib.auth.hashers import check_password
# Create your views here.
def index(request):
    return render(request,'index.html')
def loginuser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=email)
        if check_password(password, user.password) and email==user.email:
            login(request, user)
            
            request.session['user_id']=user.id
            return redirect('dash')
    return render(request, 'login.html')
   
def register(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if user with the email already exists
        if User.objects.filter(email=email).exists():

            messages.error(request, 'Email already registered')
            return render(request, 'register.html')

        # Create new user
        user = User.objects.create(
        name=name,
        email=email,
        password=make_password(password)  # Hashing the password before saving it
        )
        user.save()

        messages.success(request, 'User registered successfully')
        return redirect('loginuser')  # Redirect to l
    return render(request,'register.html')
def dash(request):
   user_id = request.session.get('user_id')
   if user_id:
        userobj = User.objects.get(id=user_id)  # Retrieve the User object from the database
        user_data = {
                'id': userobj.id,
                'name': userobj.name,
                'email': userobj.email,
                # Add more fields as needed
            }
        return render(request,'dash.html',{'user_data':user_data})
   else:
       return redirect('loginuser')
def allusers(request):
    user_id = request.session.get('user_id')
    if user_id:
        members=User.objects.exclude(id=user_id).values()
        data={
            'members':members
        }
        return render(request,'allusers.html',{'data':data})
    else:
        return redirect('loginuser')

def logoutuser(request):
    
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
        # Redirect to the homepage or login page
    return redirect('index')
