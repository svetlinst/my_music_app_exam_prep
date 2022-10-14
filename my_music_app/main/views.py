from django.shortcuts import render, redirect

from my_music_app.album.models import Album
from my_music_app.profiles.forms import ProfileForm
from my_music_app.profiles.models import Profile


def show_home_page(request):
    is_registered = True if Profile.objects.all().count() > 0 else False
    if not is_registered:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home_page')
        else:
            form = ProfileForm()

        context = {
            'form': form,
        }
        return render(request, 'core/home-no-profile.html', context)
    else:
        albums = Album.objects.all()
        context = {
            'albums': albums,
        }
        return render(request, 'core/home-with-profile.html', context)
