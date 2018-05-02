from django.shortcuts import render
from jobs.models import Jobs
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView



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
    jobs = Jobs.objects.filter(user=request.user)

    context = {
        'jobs': jobs,

    }
    return render(request, "profile.html", context)


class JobsCreate(CreateView):
    model = Jobs
    fields = ['name', 'description', 'skills', 'currency', 'budget']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobsCreate, self).form_valid(form)

    success_url = '/jobs/profile/'