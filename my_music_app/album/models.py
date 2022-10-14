from django.core.validators import MinValueValidator
from django.db import models


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_NAME_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30

    TYPE_CHOICE_POP_MUSIC = 'pop music'
    TYPE_CHOICE_JAZZ_MUSIC = 'jazz music'
    TYPE_CHOICE_RNB_MUSIC = 'r&b music'
    TYPE_CHOICE_ROCK_MUSIC = 'rock music'
    TYPE_CHOICE_COUNTRY_MUSIC = 'country music'
    TYPE_CHOICE_DANCE_MUSIC = 'dance music'
    TYPE_CHOICE_HIP_HOP_MUSIC = 'hip hop music'
    TYPE_CHOICE_OTHER = 'other'

    TYPE_CHOICES = (
        (TYPE_CHOICE_POP_MUSIC, 'Pop Music'),
        (TYPE_CHOICE_JAZZ_MUSIC, 'Jazz Music'),
        (TYPE_CHOICE_RNB_MUSIC, 'R&B Music'),
        (TYPE_CHOICE_ROCK_MUSIC, 'Rock Music'),
        (TYPE_CHOICE_COUNTRY_MUSIC, 'Country Music'),
        (TYPE_CHOICE_DANCE_MUSIC, 'Dance Music'),
        (TYPE_CHOICE_HIP_HOP_MUSIC, 'Hip Hop Music'),
        (TYPE_CHOICE_OTHER, 'Other'),
    )

    album_name = models.CharField(
        max_length=ALBUM_NAME_MAX_LENGTH,
        null=False,
        blank=False,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_NAME_MAX_LENGTH,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        null=False,
        blank=False,
        choices=TYPE_CHOICES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0),
        ],
    )
