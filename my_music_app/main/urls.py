from django.urls import path

from my_music_app.main.views import show_home_page

urlpatterns = (
    path('', show_home_page, name='home_page'),
)