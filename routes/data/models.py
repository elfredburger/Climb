from django.db import models

# Create your models here.
class Bolted_By(models.Model):
    name=models.CharField(max_length=50,help_text='enter Name of bolter',verbose_name='Name of creator',default='Unknown')
    def __str__(self):
        return self.name
class Grade(models.Model):
    grade=models.CharField(max_length=10,help_text='enter the grade of the route', verbose_name='route grade',default='Unknown')
    def __str__(self):
        return self.grade
class Location(models.Model):
    location=models.CharField(max_length=50,help_text='enter the area this route belongs to',verbose_name='area',default='Unknown')
    additional_info=models.CharField(max_length=1000,help_text='add info about parking, frest water etc',verbose_name='additional info',default='No info')
    def __str__(self):
        return self.location
class Comf(models.Model):
    comfort=models.IntegerField(help_text='comfort level from 1 to 10',verbose_name='comfort level of bolting',default=5)
    def __str__(self):
        return str(self.comfort)
class Sector(models.Model):
    location = models.ForeignKey('Location',max_length=50,help_text='enter the area this route belongs to',verbose_name='area',on_delete=models.CASCADE)
    sector=models.CharField(help_text='sector where route is located',verbose_name='sector',max_length=30,default='Unknown')
    def __str__(self):
        return self.sector
class Route(models.Model):
    name=models.CharField(max_length=50,help_text='enter name of the route',verbose_name='route name',default='Unknown')
    bolter =models.ManyToManyField('Bolted_by',verbose_name='bolter',help_text='Choose bolter',default='Unknown')
    grade=models.ForeignKey('Grade',verbose_name='grade',help_text='enter grade',on_delete=models.SET_DEFAULT,default='Unknown')
    location = models.ForeignKey('Location',verbose_name='Location',help_text='location',default='Unknown',on_delete=models.CASCADE)
    comfort=models.ForeignKey('Comf',help_text='comfort level from 1 to 10',verbose_name='comfort level of bolting',on_delete=models.SET_DEFAULT,default=5)
    rope_len=models.IntegerField(verbose_name='Rope Length',help_text='rope length',default=60)
    quickdraws=models.IntegerField(verbose_name='quickdraws',help_text='number of quickdraws',default=16)
    coords=models.URLField(max_length=1000,verbose_name='Link to goole maps',help_text='Paste url with pin of the route from goole maps',blank=True)
    extra_info=models.CharField(max_length=300,help_text='additional info about the route',blank=True)
    sector=models.ForeignKey('Sector',help_text='sector where route is located',verbose_name='sector',max_length=30, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.name
class User(models.Model):
    name = models.CharField(max_length=20,help_text='Enter first name', verbose_name='First name',blank=True)
    second_name=models.CharField(max_length=20,help_text='Enter second name', verbose_name='Second name',blank=True)
    username =models.CharField(unique=True,max_length=20,help_text='Enter username',verbose_name='Username')
    password=models.CharField(max_length=20,help_text='Enter your password',verbose_name='Password')
    age=models.IntegerField(verbose_name='Age', help_text='Enter age',blank=True)
    routes_climbed=models.ManyToManyField('Route',verbose_name='List of routes already climbed',help_text='Choose routes already climbed',blank=True)
    date_registered=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username




