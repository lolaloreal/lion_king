from django.shortcuts import render, redirect
from . models import Trip
from django.contrib import messages

# Create your views here.
def index(request):
    print 'i am index'
    return render(request, 'python_exam_app/index.html')

def travel(request):
    print 'i am travel'
    context = {
        'trips': Trip.objects.all()
    }
    return render(request, 'python_exam_app/travel.html', context)

def travel_add(request):
    print 'i am travel_add'
    return render(request, 'python_exam_app/travel_add.html')

def add(request):
    print 'i am add', request.POST
    results = Trip.objects.add(request.POST)
    print results['status']
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect ('/travel_add')
    messages.success(request, 'you made plans')
    return redirect('/travel')

def destination(request):
    print 'i am destination'
    context = {
        'trip': Trip.objects.filter()
    }
    return render(request, 'python_exam_app/destination.html', context)

def destination_place(request):
    print 'i am specific trip (destination_place)'

def logout(request):
    request.session.clear()
    messages.success(request, "you are logged out")
    return redirect('/')
