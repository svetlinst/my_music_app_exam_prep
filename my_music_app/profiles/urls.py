from django.urls import path

from my_music_app.profiles.views import profile_detail, profile_delete

urlpatterns = (
    path('details/', profile_detail, name='profile_detail'),
    path('delete/', profile_delete, name='profile_delete'),
)