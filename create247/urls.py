from django.conf.urls import include, url
from django.contrib import admin
from .import views  # this is taking any information from views.py
#from jobs import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^$', views.index, name='index'),  # used to display main homepage named index.html

    url(r'^jobs/', include('jobs.urls')),  # gives access to urls to jobs app



    #url('^', include('django.contrib.auth.urls')),  # used for templates/registration displays login page and register

    #url(r'^login/$', auth_views.login, name='login'),


    url(r'^accounts/', include('registration.backends.default.urls')),  # both urls are required for access to register,

    url(r'^accounts/', include('django.contrib.auth.urls')), # both urls are required for access to login and password

    url(r'^admin/', include(admin.site.urls)),
]
