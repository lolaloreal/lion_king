from django.shortcuts import render, redirect
from django.contrib import messages
from . models import User
from django.contrib import messages

# Create your views here.

def index(request):
    print 'i am index'
    return render(request, 'belt_login_app/index.html')

def success(request):
    print "SUCCESS!"
    context = {
        'username' : request.session['username']
    }
    return render(request, 'belt_login_app/success.html')

def login(request):
    print "Login works"
    user_objects = User.objects.UserExistsLogin(request.POST)
    if user_objects['status']:
        messages.success(request, "hello!")
        # request.session['first_name'] = request.POST['first_name']
        return redirect('/travel')
    else:
        #user_objects['status'] = False
        #if results['status'] == False:
        for error in user_objects['errors']:
            messages.error(request, error)
        return redirect('/')

def register(request):
    print "Register works"
    user_objects = User.objects.isValidRegistration(request.POST)
    if user_objects['status']:
        request.session['username'] = request.POST['username']
        messages.success(request, "hello. you are registered!")
        #user_objects['status'] = True
        return redirect('/travel')
    else:
        #user_objects['status'] = False
        #if user_objects['status'] == False:
        for error in user_objects['errors']:
            messages.error(request, error)
        return redirect('/')
