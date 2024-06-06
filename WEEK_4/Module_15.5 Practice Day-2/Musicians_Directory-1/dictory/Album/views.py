from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

def album_list(request):
    albums = Album.objects.select_related('Musician').all()
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
    album = AlbumForm(Album, pk=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')

    return render(request, 'album_form.html', {'form': form,'flag' : True}  )

def album_delete(request, id):
    album = Album.objects.get(Album, pk=id)
    album.delete()
    return redirect('album_list')


