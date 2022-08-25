from contextlib import redirect_stderr
from urllib import response
from urllib.request import urlcleanup
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def hello(response):
    return render(response, "app/hello.html", {})

def exp(response):
    return render(response, "app/exp.html", {})   

def proj(response):
    return render(response,"app/proj.html",{} )

def skills(response):
    return render(response,"app/skills.html",{}) 

def contact(response):
    return render(response, "app/contact.html",{})

def degree(response):
    return render(response, "app/study.html",{})
