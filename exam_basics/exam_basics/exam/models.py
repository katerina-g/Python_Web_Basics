from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_basics.exam.validators import validate_only_letters_nums_underscore


class Profile(models.Model):
    USERNAME_MIN_LEN = 2
    USERNAME_MAX_LEN = 15

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            validate_only_letters_nums_underscore,
        )
    )
    email = models.EmailField()
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_NAME_MAX_LEN = 30

    album_name = models.CharField(
        max_length=ALBUM_NAME_MAX_LEN,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
    )
    genre = models.CharField(
        max_length=GENRE_NAME_MAX_LEN,
        choices=(
            ('Pop Music', 'Pop Music'),
            ('Jazz Music', 'Jazz Music'),
            ('R&B Music', 'R&B Music'),
            ('Rock Music', 'Rock Music'),
            ('Country Music', 'Country Music'),
            ('Dance Music', 'Dance Music'),
            ('Hip Hop Music', 'Hip Hop Music'),
            ('Other', 'Other'),
        )
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField()
    price = models.FloatField(
        validators=(MinValueValidator(0),)
    )
