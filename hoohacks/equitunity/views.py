from django.shortcuts import render

# Create your views here.


def home(request):
      # Return the home page
    return render(request, 'home.block.html')

def login(request):
      # Return the login page
    return render(request, 'login.block.html')

def signup(request):
      # Return the signup page
    return render(request, 'signup.block.html')

def user_profile(request):
      # Return the user profile page
    return render(request, 'userProfile.block.html')

def school_profile(request):
      # Return the school profile page
    return render(request, 'schoolProfile.block.html')
