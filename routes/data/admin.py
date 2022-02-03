from django.contrib import admin
from .models import Bolted_By,Route,Grade,Comf,Location,Sector,Boulder

# Register your models here.
admin.site.register(Bolted_By)
admin.site.register(Route)
admin.site.register(Grade)
admin.site.register(Sector)
admin.site.register(Comf)
admin.site.register(Location)
admin.site.register(Boulder)