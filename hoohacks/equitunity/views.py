from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
import json 
from .models import *
import requests
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
    print(result)
      # Return the user profile page
    return render(request, 'user_profile.block.html',
      {'nameFirst':user['first_name'], 'nameLast':user['last_name'], 'email':user['email'], 'inCollege':result['inCollege'],
      'collegeCode':school.actCode, 'major':result['major'], 'SecondMaj':result['secondMaj'], 'minor':result['minor'],
      'seconMin':result['secondMin'],
      'majors':[{"pk":1,"name":"Computer Science"}, {"pk":2,"name":"Computer Engineering"}, {"pk":3,"name":"Statistics"}],
      'hometown':result['hometown'], 'bio':result['bio']})

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
    passw = request.POST.get('inputPassword')
    confp = request.POST.get('confirmPassword')
    print('data is', data)
    print("\n PASSWORDS", passw, confp)
    if(passw!=confp):
      print("Passwords don't match")
      return render(request, 'signup.block.html', {'error':True})
    
    username = request.POST.get('inputEmail')
    first_name = request.POST.get('firstName')
    last_name = request.POST.get('lastName')
    password = passw
    email = request.POST.get('inputEmail')
    user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
    dob = request.POST.get('dob')
    if(request.POST.get('accountType')=="college"):
      inCollege=True
    else:
      inCollege=False
    Student.objects.create(user=user, dob=dob, inCollege=inCollege)
    # get each item individually
    return render(request, 'user_profile.block.html')
  else:
    print('You should make sure you have the right form method')
  return render(request, 'user_profile.block.html')
