from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'Album': albums})


def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form': form,'flag' : False})

def album_edit(request, id):
    album = Album.objects.get(pk=id)
    album_form = AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('album_list')

    return render(request, 'album_form.html', {'form': album_form,'flag' : True})

def album_delete(request, id):
    album = Album.objects.get(id=id)
    album.delete()
    return redirect('album_list')


