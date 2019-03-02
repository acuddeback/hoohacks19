from django.shortcuts import render
import json 
import requests
from .models import *
# Create your views here.


def home(request):
      # Return the home page
    return render(request, 'home.block.html')

def login(request):
      # Return the login page
    return render(request, 'login.block.html')

def signup(request):
      # Return the signup page
    print('hitting here')
    return render(request, 'signup.block.html')

def user_profile(request, pk):
    data = requests.get('http://localhost:8000/api/student/'+str(pk))
      # Store the data
    data = json.loads((data.text))
    result = data['result']
    user = result['user']
    school = School.objects.get(pk=result['college'])
      # Return the user profile page
    return render(request, 'user_profile.block.html',
      {'nameFirst':user['first_name'], 'nameLast':user['last_name'], 'email':user['email'], 'inCollege':result['inCollege'],
      'collegeCode':school.actCode, 'major':"Statistics",
      'majors':[{"pk":1,"name":"Computer Science"}, {"pk":2,"name":"Computer Engineering"}, {"pk":3,"name":"Statistics"}],
      'hometown':"Virginia Beach", 'bio':"Blah blah blah"})

def school_profile(request):
      # Return the school profile page
    return render(request, 'school_profile.block.html')

def terms(request):
    # Return the terms and conditions page
  return render(request, 'terms.block.html')

def signup_submit(request):
    # Subpostmit information from signup form
  print ('RECEIVED REQUEST YO: ' + request.method)
  if request.method == 'POST':
    print ('WE GOT STUFF: ', request.POST)
    data = request.POST
    # get each item individually
    print('data is', data)
  else:
    print('You should make sure you have the right form method')
  return render(request, 'user_profile.block.html')
