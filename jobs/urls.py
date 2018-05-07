from django.conf.urls import url
#app_name = "jobs"
from.import views


urlpatterns = [


    #url(r'^$', views.jobs, name='jobs'),  # used to display main homepage named index.html


    # this does not re-direct to templates/jobs/profile but to templates/profile.html
    url(r'^profile/$', views.profile, name='profile'),

    url(r'^add/$', views.JobsCreate.as_view(), name='jobs-add'),
    url(r'^add/$', views.JobsCreate.as_view(), name='jobs-update'),

    #url(r'^update/$', views.JobsUpdate.as_view(), name='jobs-update'),


    url(r'^update/(?P<pk>[0-9]+)/$', views.JobsUpdate.as_view(), name='jobs-update'),




]
