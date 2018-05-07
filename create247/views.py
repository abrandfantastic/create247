from django.http import HttpResponse  # when used will write text to web page
from django.shortcuts import render

# uses the from django.http import HttpResponse

def index(request):
    # return HttpResponse('test 123') # only write text to page

    return render(request,'index.html') # this displays html page from templates/index.html

"""
index.html is using a base.html which contains css
"""

