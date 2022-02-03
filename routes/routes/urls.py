from data import views
"""routes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('routes_list/',views.routes_list_view,name='routes_list_view'),
    path('bolters_list/',views.bolters_list_view,name='bolters_list_view'),
    path('comfs_list/',views.comfs_list_view,name='comfs_list_view'),
    path('grades_list/',views.grades_list_view,name='grades_list_view'),
    path('locations_list/',views.locations_list_view,name='locations_list_view'),
    path('sectors_list/',views.sectors_list_view,name='sectors_list_view'),
    path('boulders_list/',views.boulders_list_view,name='boulders_list_view'),
    path('add_bolter/',views.add_bolter_view,name='add_bolter_view'),
    path('add_location/',views.add_location_view,name='add_location_view'),
    path('add_route/',views.add_route_view,name='add_route_view'),
    path('add_sector/',views.add_sector_view ,name='add_sector_view'),
    path('add_comf/',views.add_comf_view,name='add_comf_view'),
    path('add_grade/',views.add_grade_view,name='add_grade_view'),
    path('add_boulder/',views.add_boulder,name='add_boulder'),
    path('routes_list/edit_route/<int:id>/',views.edit_route,name='edit_route'),
    path('routes_list/delete_route/<int:id>',views.delete_route,name='delete_route'),
    path('bolters_list/edit_bolter/<int:id>',views.edit_bolter,name='edit_bolter'),
    path('bolters_list/delete_bolter/<int:id>',views.delete_bolter,name='delete_bolter'),
    path('locations_list/edit_location/<int:id>',views.edit_location,name='edit_location'),
    path('locations_list/delete_location/<int:id>',views.delete_location, name='delete_location'),
    path('sectors_list/edit_sector/<int:id>',views.edit_sector,name='edit_sector'),
    path('sectors_list/delete_sector/<int:id>',views.delete_sector,name='delete_sector'),
    path('comfs_list/edit_comf/<int:id>',views.edit_comf,name='edit_comf'),
    path('comfs_list/delete_comf/<int:id>',views.delete_comf,name='delete_comf'),
    path('grades_list/edit_grade/<int:id>',views.edit_grade,name='edit_grade'),
    path('grades_list/delete_grade/<int:id>',views.delete_grade,name='delete_grade'),
    path('register_user/',views.register_user,name='register_user'),
    path('login_page/',views.login_page,name='loin_page'),
    path('logout/',views.logout_user,name='logout_user'),
    path('index/',views.index)

]
