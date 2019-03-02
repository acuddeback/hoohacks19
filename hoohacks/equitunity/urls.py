from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'login/$', views.login, name='login'),
    url(r'signup/$', views.signup, name='signup'),
    url(r'user_profile/$', views.userProfile, name='user_profile'),
    url(r'school_profile/$', views.schoolProfile, name='school_profile')
]
