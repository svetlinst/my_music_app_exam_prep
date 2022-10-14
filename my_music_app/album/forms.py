from django import forms

from my_music_app.album.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                },
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                },
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                },
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                },
            ),
        }


class EditAlbum(AlbumForm):
    pass


class DeleteAlbum(AlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
