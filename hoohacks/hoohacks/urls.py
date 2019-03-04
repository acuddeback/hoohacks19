"""hoohacks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from equitunity import views, api_views

# View sets have default methods for handling GET/POST/etc, so this is explicitly overriding that
request_override_map = {
    'get': 'get',
    'post': 'post',
    'put': 'put',
    'delete': 'delete'
}

# Set up seriallizers
student_list = api_views.StudentViewSet.as_view(request_override_map)
school_list = api_views.SchoolViewSet.as_view(request_override_map)
ratio_list = api_views.RatioViewSet.as_view(request_override_map)
major_list = api_views.MajorViewSet.as_view(request_override_map)

urlpatterns = [
    # Main website
    url(r'^admin/', admin.site.urls),
    url(r'^', include('equitunity.urls')),

    # Api
    # Get one Student
    url(r'^api/student/(?P<pk>[0-9]+)', student_list, name='student-detail'),
    # Get all student
    url(r'^api/student/', student_list, name='student-list'),
   
    # Get one School
    url(r'^api/school/(?P<pk>[0-9]+)', school_list, name='school-detail'),
    # Get all School
    url(r'^api/school/', school_list, name='school-list'),
   
    # Get one Major
    url(r'^api/major/(?P<pk>[0-9]+)', major_list, name='major-detail'),
    # Get all Major
    url(r'^api/major/', major_list, name='major-list'),
    
    # Get one Ratio
    url(r'^api/ratio/(?P<pk>[0-9]+)', ratio_list, name='ratio-detail'),
    # Get all Ratio
    url(r'^api/ratio/', ratio_list, name='ratio-list'),
]
