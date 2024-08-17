from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Web empresarial</h1>")

def about(request):
    return HttpResponse("<h1>Web empresarial</h1>")

def services(request):
    return HttpResponse("<h1>Web empresarial</h1>")

def store(request):
    return HttpResponse("<h1>Web empresarial</h1>")

def contact(request):
    return HttpResponse("<h1>Web empresarial</h1>")

def blog(request):
    return HttpResponse("<h1>Web empresarial</h1>")

def sample(request):
    return HttpResponse("<h1>Web empresarial</h1>")