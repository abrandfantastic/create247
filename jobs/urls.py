from django.conf.urls import url
app_name = "jobs"
from . import views

urlpatterns = [
    #url(r'^$', views.profile, name='profile'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^home/$', views.home),

    url(r'^add/$', views.JobsCreate.as_view(), name='jobs-add'),

]