from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from my_music_app.profiles.validators import validate_username_characters


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(2),
            validate_username_characters,
        ]
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(2),
        ]
    )