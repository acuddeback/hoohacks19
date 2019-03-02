from django.shortcuts import render
import json 
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

def user_profile(request):
      # Return the user profile page
    return render(request, 'user_profile.block.html', {'nameFirst':"Will", 'nameLast':"Scheib", 'email':"wms9gv@virginia.edu", 'inCollege':True})

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
    print ('WE GOT STUFF: ', request.body)
  else:
    print('You should make sure you have the right form method')
  return render(request, 'user_profile.block.html')
