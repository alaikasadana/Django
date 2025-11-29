print("views pagr call")

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def landingpage(req):
    # return HttpResponse("hello this is django project")
    # return HttpResponse("<h1 style='color:yellow;'>hello this is django project</h1>")
    return HttpResponse("<h1>hello this is django project</h1>")