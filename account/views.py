from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from jobapp.models import Applicants
from .models import Profile
from .forms import UpdateProfile
import random

# Create your views here.

def register(request):
    template_name = 'accounts/register.html'

    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            uname = request.POST['uname']
            email = request.POST['email']
            pw = request.POST['pw']
            name = request.POST['name']
            surname = request.POST['surname']

            if is_registrable(uname, email):
                user = User.objects.create_user(username=uname, email=email, password=pw, first_name=name, last_name=surname)
                user.save()
                return redirect('login')
            else:
                return render(request, template_name, {'error':'User already exist'})

    return render (request, template_name)

def login(request):
    template_name = 'accounts/login.html'

    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            uname = request.POST['uname']
            password = request.POST['pw']

            user = auth.authenticate(username = uname, password = password)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                return render(request, template_name, {'error':'Username or password is wrong'})
    
    return render(request, 'accounts/login.html')

@login_required(login_url='/account/login')
def logout(request):
    auth.logout(request)

    return redirect('index')

def is_registrable(uname, email):
    isRegistrable = False

    if User.objects.filter(username=uname).exists():
        isRegistrable = False
    else:
        if User.objects.filter(email=email).exists():
            isRegistrable = False
        else:
            isRegistrable = True
    
    return isRegistrable

def reset_pw(request):
    if request.method == 'POST':
        email = request.POST['email']
        global key
        key = random.randint(100000, 1000000)
        
        if email:
            try:
                send_mail(
                    'Reset Password',
                    f'password reset key = {key}',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header')
        else:
            return HttpResponse('Invalid email address')
    else:
        redirect('forgot_pw')

    return render(request, 'accounts/reset_password.html')

def forgot_pw(request):
    template_name = 'accounts/forgot_pw.html'

    return render(request, template_name, {'info': 'Please enter your registered email address in the system'})

def confirm(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pw = request.POST['pw']
        _key = request.POST['_key']

        if pw and _key:
            if int(_key) == key:
                user = User.objects.get(username=uname)
                user.set_password(pw)
                user.save()

                return redirect('login')
            else:
                return redirect('forgot_pw')
        else:
            return HttpResponse('Invalid password or key')

@login_required(login_url='/account/login')
def profile(request):
    user = request.user
    template_name = 'accounts/profile.html'

    context = {
        
    }

    if Profile.objects.filter(user=user).exists():
        query = Profile.objects.get(user=user)
        update_profile = UpdateProfile(instance=query)
        context['user_profile'] = query
    else:
        update_profile = UpdateProfile()

    if request.method == 'POST':
        update_profile = UpdateProfile(request.POST, request.FILES)
        
        if update_profile.is_valid():
            new_profile = update_profile.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
    
    context['update_profile'] = update_profile

    return render(request, template_name, context)

@login_required(login_url='/account/login')
def delete_account(request, id):
    if Applicants.objects.filter(user=request.user).exists():
        Applicants.objects.filter(user=request.user).delete()
    if Profile.objects.filter(user=request.user).exists():
        Profile.objects.get(user=request.user).delete()
    
    auth.logout(request)

    User.objects.get(id=id).delete()
    
    return redirect('index')