from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def welcome(request):
   
    return render(request, 'index.html')