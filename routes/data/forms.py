from django import forms
from .models import Bolted_By,Location,Sector,Route,Grade,Comf,Boulder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GradeForm(forms.ModelForm):
    class Meta:
        model=Grade
        fields=['grade']
class ComfForm(forms.ModelForm):
    class Meta:
        model=Comf
        fields=['comfort']
    def clean_comfort(self):
        comfort=self.cleaned_data.get('comfort')
        if comfort not in range(0,11):
            raise forms.ValidationError('Incorrect amount, should be between 1 and 10')
        else:return comfort
class BoltedByForm(forms.ModelForm):
    class Meta:
        model=Bolted_By
        fields=['name']
class GradeForm(forms.ModelForm):
    class Meta:
        model=Grade
        fields=['grade']
class LocationForm(forms.ModelForm):
    additional_info = forms.CharField(label='Доп информация',widget=forms.Textarea(attrs={'rows': 6, 'cols': 20}))

    class Meta:
        model=Location
        fields=['location','additional_info']
class SectorForm(forms.ModelForm):
    class Meta:
        model=Sector
        fields=['location','sector']
class RouteForm(forms.ModelForm):
    class Meta:
        model=Route
        fields=['name','bolter','grade','location','comfort','rope_len','quickdraws','coords','extra_info','sector']
    def clean_rope_len(self):
        rope_len=self.cleaned_data.get('rope_len')
        if int(rope_len) > 200:
            raise forms.ValidationError('Supported length is up to 200m, please lower the value')
        if int(rope_len) <10:
            raise forms.ValidationError('Supported length starts with 10m, please increase the value')
        else: return rope_len
    def clean_coords(self):
        coords=self.cleaned_data.get('coords')
        if 'www.google.com/maps/place/' not in coords:
            raise forms.ValidationError('Not a valid location')
        else: return coords
    def clean_quickdraws(self):
        quickdraws=self.cleaned_data.get('quickdraws')
        if quickdraws not in range(1,25):
            raise forms.ValidationError('Quickdraws amount is incorrect, make sure it is in the range from 2 to 25')
        else:return quickdraws
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class BoulderForm(forms.ModelForm):
    class Meta:
        model=Boulder
        fields='__all__'
    def clean_height(self):
        heigth=self.cleaned_data.get('height')
        if int(heigth) not in range(1,15):
            raise  forms.ValidationError('Heigth ins incorrect, make sure it is in the range from 1 to 15')
        else:return heigth
    def clean_coords(self):
        coords=self.cleaned_data.get('coords')
        if 'www.google.com/maps/place/' not in coords:
            raise forms.ValidationError('Not a valid location')
        else: return coords
    def clean_amount_of_crashpads(self):
        amount_of_crashpads=self.cleaned_data.get('amount_of_crashpads')
        if amount_of_crashpads not in range(0,20):
            raise  forms.ValidationError('Amount of crashpads is incorrect, make sure it is in the range from 0 to 20')
        else: return amount_of_crashpads