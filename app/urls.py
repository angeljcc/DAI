__author__ = 'angel'

from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^$', views.index,name='main'),
    url(r'profile$',views.profile,name='profile'),
    url(r'signup$',views.signup,name='signup'),
    url(r'login$',views.login,name='login'),
    url(r'logout$',views.logout,name='logout'),
    url(r'invalid$',views.invalid,name='invalid'),
    url(r'thanks$',views.thanks,name='invalid'),
]