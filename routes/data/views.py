from django.shortcuts import render, get_object_or_404,redirect
from .models import Route,Bolted_By,Grade,Sector,Location,Comf,Boulder
from django.contrib import messages
from .decorators import unauth_user,allowed_users
from .forms import BoltedByForm,RouteForm,LocationForm,SectorForm,GradeForm,ComfForm,CreateUserForm,BoulderForm
from  django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def routes_list_view(request):
    data=Route.objects.all()
    return render(request,'routes_list.html',{'data':data})



def bolters_list_view(request):
    data=Bolted_By.objects.all()
    return render(request,'bolters_list.html',{'data':data})

def comfs_list_view(request):
    data=Comf.objects.all()
    return render(request,'comfs_list.html',{'data':data})

def grades_list_view(request):
    data=Grade.objects.all()
    return render(request,'grades_list.html',{'data':data})

def locations_list_view(request):
    data=Location.objects.all()
    return render(request,'locations_list.html',{'data':data})

def sectors_list_view(request):
    data=Sector.objects.all()
    return render(request,'sectors_list.html',{'data':data})
def boulders_list_view(request):
    data=Boulder.objects.all()
    return render(request,'boulders_list.html',{'data':data})

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['contributor','content_staff'])
def add_bolter_view(request):
    form=BoltedByForm(request.POST or None)
    if form.is_valid():
        form.save()
    data={'form':form}
    return render(request,'add_bolter.html',data)

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['contributor','content_staff'])
def add_location_view(request):
    form=LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
    data={'form':form}
    return render(request,'add_location.html',data)

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['contributor','content_staff'])
def add_sector_view (request):
    form=SectorForm(request.POST or None)
    if form.is_valid():
        form.save()
    data={'form':form}
    return render(request,'add_sector.html',data)


@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['contributor','content_staff'])
def add_route_view(request):
    form=RouteForm(request.POST or None)
    if form.is_valid():
        form.save()
    data={'form':form}
    return  render(request,'add_route.html',data)

@login_required(login_url='../login_page')
def index(request):
    return render(request,'index.html',{})

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def add_grade_view(request):
    form=GradeForm(request.POST or None)
    if form.is_valid():
        form.save()
    data={'form':form}
    return render(request,'add_grade.html',data)


@allowed_users(allowed_roles=['contributor','content_staff'])
def add_boulder(request):
    form = BoulderForm(request.POST or None)
    if form.is_valid():
        form.save()
    data = {'form': form}
    return render(request, 'add_boulder.html', data)

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def add_comf_view(request):
    form=ComfForm(request.POST or None)
    if form.is_valid():
        form.save()
    data={'form':form}
    return render(request,'add_comf.html',data)

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def edit_route(request,id):
    route=Route.objects.get(id=id)
    form=RouteForm(request.POST or None, instance=route)
    get_object_or_404(Route,id=id)
    if form.is_valid():
        form.save()
    data={'form':form}
    return render(request,'edit_route.html',data)

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def delete_route(request,id):
    route=Route.objects.get(id=id)
    route.delete()
    return redirect('../../routes_list')

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def edit_bolter(request,id):
    bolter=Bolted_By.objects.get(id=id)
    form=BoltedByForm(request.POST or None, instance=bolter)
    get_object_or_404(Bolted_By,id=id)
    if form.is_valid():
        form.save()
    data={'form':form}
    return render(request,'edit_bolter.html',data)

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def delete_bolter(request,id):
    bolter=Bolted_By.objects.get(id=id)
    bolter.delete()
    return redirect('../../bolters_list')

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def edit_location(request,id):
    location=Location.objects.get(id=id)
    form=LocationForm(request.POST or None,instance=location)
    get_object_or_404(Location,id=id)
    if form.is_valid():
        form.save()
    data={'form':form}
    return render(request,'edit_location.html',data)




@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def delete_location(request,id):
    location=Location.objects.get(id=id)
    location.delete()
    return redirect('../../locations_list')


@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def edit_sector(request,id):
    sector=Sector.objects.get(id=id)
    form=SectorForm(request.POST or None, instance=sector)
    get_object_or_404(Location,id=id)
    if form.is_valid():
        form.save()
    data={'form':form}
    return render(request,'edit_sector.html',data)

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def delete_sector(request,id):
    sector=Sector.objects.get(id=id)
    sector.delete()
    return redirect('../../sectors_list')

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def edit_comf(request,id):
    comf=Comf.objects.get(id=id)
    form=ComfForm(request.POST or None,instance=comf)
    get_object_or_404(Comf,id=id)
    if form.is_valid():
        form.save()
    data={'form':form}
    return render(request,'edit_comf.html',data)

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def delete_comf(request,id):
    comf=Comf.objects.get(id=id)
    comf.delete()
    return redirect('../../comfs_list')

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def edit_grade(request,id):
    grade=Grade.objects.get(id=id)
    form = GradeForm(request.POST or None, instance=grade)
    get_object_or_404(Grade,id=id)
    if form.is_valid():
        form.save()
    data={'form':form}
    return render(request,'edit_grade.html',data)

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def delete_grade(request,id):
    grade=Grade.objects.get(id=id)
    grade.delete()
    return redirect('../../grades_list')
@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def edit_boulder(request,id):
    boulder=Boulder.objects.get(id=id)
    form=BoulderForm(request.POST or None,instance=boulder)
    get_object_or_404(Boulder,id=id)
    if form.is_valid():
        form.save()
    data={'form':form}
    return renderer(request,'edit_boulder.html',data)

@login_required(login_url='../login_page')
@allowed_users(allowed_roles=['content_staff'])
def delete_boulder(request,id):
    boulder=Boulder.objects.get(id=id)
    boulder.delete()
    return redirect('../../boulders_list')
@login_required(login_url='../login_page')

@unauth_user
def register_user(request):

    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get('username')
            messages.success(request,'Аккаунт создан '+user)
            return redirect('../login_page')
    data={'form':form}
    return render(request,'register_user.html',data)

@unauth_user
def login_page(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('../index')
        else: messages.info(request,'Логин или пароль введен не верно!')

    data={}
    return render(request,'login_page.html',data)

@login_required(login_url='../login_page')
def logout_user(request):
    logout(request)
    return redirect('../login_page')
