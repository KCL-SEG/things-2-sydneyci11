"""Forms of the project."""
from django import forms
from .models import Thing
# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(max_length=35)
    description = forms.Textarea(attrs={'rows':3, 'cols': 5})
    quantity = forms.IntegerField()