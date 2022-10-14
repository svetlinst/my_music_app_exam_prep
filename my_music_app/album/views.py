from django.shortcuts import render, redirect

from my_music_app.album.forms import AlbumForm, EditAlbum, DeleteAlbum
from my_music_app.album.models import Album


def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = AlbumForm()

    context = {
        'form': form,
    }
    return render(request, 'album/add-album.html', context)


def show_details(request, id):
    album = Album.objects.filter(pk=id).get()
    context = {
        'album': album,
    }

    return render(request, 'album/album-details.html', context)


def edit_album(request, id):
    album = Album.objects.get(pk=id)
    if request.method == 'POST':
        form = EditAlbum(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = EditAlbum(instance=album)

    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'album/edit-album.html', context)


def delete_album(request, id):
    album = Album.objects.get(pk=id)
    if request.method == 'POST':
        album.delete()
        return redirect('home_page')
    else:
        form = DeleteAlbum(instance=album)

    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'album/delete-album.html', context)

