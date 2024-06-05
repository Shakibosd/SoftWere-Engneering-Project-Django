
from django.shortcuts import render, redirect
from musician.forms import MusicianForm
from musician.models import Musician

def musician_form(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MusicianForm()
    return render(request, 'musician/musician.html', {'musicians': form, 'flag' : False})

def edit_musician(request, pk):
    user = Musician.objects.get(pk = pk)
    user_form = MusicianForm(instance=user)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('home')
        
    return render(request, 'musician/musician.html', {'form': user_form, 'flag' : False})

def musician_delete(request, pk):
    musician = Musician.objects.get(pk = pk)
    musician.delete()
    return redirect('home')


