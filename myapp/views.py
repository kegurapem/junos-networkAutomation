from django.shortcuts import render
from nornir.app import hello

# data = hello()

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'hello': hello()
    })