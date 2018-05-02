from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'create247.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'jobs.views.home', name='home'),

    url(r'^jobs/', include('jobs.urls')),

    url('^', include('django.contrib.auth.urls')),

    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
