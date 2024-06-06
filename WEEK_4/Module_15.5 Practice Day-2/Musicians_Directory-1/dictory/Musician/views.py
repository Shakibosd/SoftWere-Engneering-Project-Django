from django.shortcuts import render, redirect
from .models import Musician
from .forms import MusicianForm

def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'musician_list.html', {'Musician': musicians})

def musician_create(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = MusicianForm()
    return render(request, 'musician_form.html',  {'form': form, 'flag' : False})

def musician_edit(request, id):
    musician = Musician.objects.get(id=id)
    musician_form = MusicianForm(instance=musician)
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('musician_list')

    return render(request, 'musician_form.html', {'form': musician_form, 'flag' : False})

def musician_delete(request, id):
    musician = Musician.objects.get(id=id)
    musician.delete()
    return redirect('musician_list')
