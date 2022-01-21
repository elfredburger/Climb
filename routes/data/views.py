from django.shortcuts import render
from .models import Route

# Create your views here.
def index(request):
    data=Route.objects.all()
    return render(request,'index.html',{'data':data})