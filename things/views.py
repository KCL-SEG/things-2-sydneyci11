from django.shortcuts import render
from django import forms
from .forms import ThingForm
from .models import Thing

def home(request):
    form = ThingForm()
    if request.method=='POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            quantity = form.cleaned_data.get('quantity')
            req = Thing(name, description, quantity)
            req.save()
            
    return render(request, 'home.html', {'form': form})
