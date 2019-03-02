from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'login/$', views.login, name='login'),
    url(r'signup/$', views.signup, name='signup'),
    url(r'user_profile/(?P<pk>[0-9]+)', views.user_profile, name='user_profile'),
    url(r'school_profile/$', views.school_profile, name='school_profile'),
    url(r'terms/$', views.terms, name='terms'),
    url(r'signup/submit$', views.signup_submit, name="signup_submit")
]
