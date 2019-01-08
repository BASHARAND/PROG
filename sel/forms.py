from django import forms
from . models import Get,Order



class Chois(forms.Form):
    count = forms.IntegerField(required=True, min_value=1, max_value=10, widget=forms.NumberInput())
  #  prod = forms.IntegerField(required=True, widget=forms.NumberInput(),label='pop')

    Ch = forms.BooleanField(initial=False,label='',required=False)
    M = forms.BooleanField(initial=True,required=False)
    K = forms.BooleanField(initial=True,required=False)
    p = forms.BooleanField(initial=True,required=False)
    S = forms.BooleanField(initial=False,required=False)
    T = forms.BooleanField(initial=True,required=False)


