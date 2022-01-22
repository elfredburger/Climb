from django.shortcuts import render
from .models import Route,User

# Create your views here.
def index(request):
    data=Route.objects.all()
    return render(request,'index.html',{'data':data})
def users(request):
    data=User.objects.all()
    return render(request,'users.html',{'data':data})