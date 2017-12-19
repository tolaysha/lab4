from django import  forms
from .models import *

class Subscruberforms(forms.ModelForm):
    class Meta:
        model = Subscribers
        exclude = [""]