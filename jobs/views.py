from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Jobs
from django.contrib.auth.decorators import login_required
from django.views import generic

# Create your views here.
"""
def home(request):
    count = Jobs.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, "home.html", context)


def index(request):
    jobs = Jobs.objects.all()

    context = {
        'jobs': jobs,

    }
    return render(request, "index.html", context)
"""

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

    success_url = 'jobs:profile'

   #success_url = reverse_lazy('index.html')

class JobsUpdate(UpdateView):
    model = Jobs
    fields = ['name', 'description', 'skills', 'currency', 'budget']

    success_url = 'jobs:profile'

