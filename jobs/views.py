from django.shortcuts import render
from jobs.models import Jobs
from django.contrib.auth.decorators import login_required



# Create your views here.
"""
def home(request):
    count = Jobs.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, "home.html", context)
"""


def home(request):
    jobs = Jobs.objects.all()

    context = {
        'jobs': jobs,

    }
    return render(request, "home.html", context)


@login_required
def profile(request):
    jobs = Jobs.objects.filter(user = request.user)

    context = {
        'jobs': jobs,

    }
    return render(request, "profile.html", context)