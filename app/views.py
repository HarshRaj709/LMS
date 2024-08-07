from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from .forms import Registration,Userlogin,ProfileUpdate
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request,'app/home.html')

def single_course(request):
    return render(request,'app/single.html')

def contact(request):
    return render(request,'app/contact.html')

def about(request):
    return render(request,'app/about_us.html')

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = Userlogin(request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                # if '@' in username_or_email:
                #     users =  User.objects.get(email = username_or_email)    #easy way to login through email
                #     username = users.username
                # else:
                #     username = username
                # print(username,password)
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('home')
                else:
                    messages.error(request,'Invalid Credentials')
                    #return redirect('login')
        else:
            fm = Userlogin()
        return render(request,'app/login.html',{'form':fm})
    else:
        return redirect('home')

def signup_user(request):
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            user = User.objects.create(username=username,email=email)
            user.set_password(password)
            user.save()
            return redirect('login')
    else:
        fm = Registration()
    return render(request,'app/signup.html',{'form':fm})

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def profile(request):
    user = request.user
    if request.method == 'POST':
        fm = ProfileUpdate(request.POST,instance = user)
        if fm.is_valid():
            user = fm.save(commit=False)
            password = fm.cleaned_data['password']
            if password is not None or password != '':
                user.set_password(password) 
                user.save()
                update_session_auth_hash(request,user)
            else:
                user.save()
            return redirect('profile')
    else:
        fm = ProfileUpdate(instance=user)
    return render(request,'app/account/profile.html',{'form':fm})