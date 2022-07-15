from django import forms
from .models import Shift
# from django.contrib.auth.models import User


class ClockInOutForm(forms.ModelForm):  #shiftForm 
  clock_in = forms.TimeField(label='Inicio ', 
                             widget=forms.TimeInput( 
                             attrs={"class":"form-control", "placeholder":"horas:min:seg"})) 
  
  clock_out = forms.TimeField(label='fim', 
                              widget=forms.TimeInput(
                              attrs={"class":"form-control", "placeholder":"horas:min:seg"}))

  

  date = forms.DateField(widget=forms.SelectDateWidget(attrs={"class":""}))

  class Meta():
    model = Shift 
    fields = ['description']


class SelectDateForm(forms.Form):
  date_from = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "",}, ), label="From")
  date_to = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "",}), label="To")


class ShiftUpdateForm(forms.Form):
  clock_in = forms.TimeField(label='Inicio ', 
                             widget=forms.TimeInput( 
                             attrs={"class":"form-control", "placeholder":"hour:min:sec"})) 
  
  clock_out = forms.TimeField(label='Fim', 
                              widget=forms.TimeInput(
                              attrs={"class":"form-control", "placeholder":"hour:min:sec"}))

 

  date = forms.DateField(widget=forms.SelectDateWidget(attrs={"class":""}))