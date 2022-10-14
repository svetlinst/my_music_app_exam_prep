from django.shortcuts import render, redirect

from my_music_app.album.models import Album
from my_music_app.profiles.models import Profile


def profile_detail(request):
    profile = Profile.objects.first()
    album_cnt = Album.objects.all().count()
    context = {
        'profile': profile,
        'album_count': album_cnt,
    }

    return render(request, 'profile/profile-details.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        albums = Album.objects.all()
        albums.delete()
        return redirect('home_page')

    return render(request, 'profile/profile-delete.html')
