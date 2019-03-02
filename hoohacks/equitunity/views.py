from django.shortcuts import render

# Create your views here.


def home(request):
      # Return the home page
    return render(request, 'home.block.html')
