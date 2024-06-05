from Album.forms import AlbumForm
from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album')
    else:
        form = AlbumForm()
    return render(request, 'Album/album.html', {'form': form,'flag' : False})

def album_edit(request, pk):
    album = AlbumForm(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'Album/album.html', {'form': form,'flag' : True})

def album_delete(request, pk):
    album = AlbumForm(Album, pk=pk)
    album.delete()
    return redirect('album')

