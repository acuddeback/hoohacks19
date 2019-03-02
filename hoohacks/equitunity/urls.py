from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home')
    url(r'^$', views.login, name='login')
    url(r'^$', views.signup, name='signup')
    url(r'^$', views.userProfile, name='userProfile')
    url(r'^$', views.schoolProfile, name='schoolProfile')
]
