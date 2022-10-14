from django.urls import path

from my_music_app.album.views import create_album, show_details, edit_album, delete_album

urlpatterns = (
    path('add/', create_album, name='create_album'),
    path('details/<int:id>/', show_details, name='show_details'),
    path('edit/<int:id>/', edit_album, name='edit_album'),
    path('delete/<int:id>/', delete_album, name='delete_album'),
)


