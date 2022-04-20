from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    email = models.EmailField()

    age = models.PositiveIntegerField(
        validators=(MinValueValidator(12),)
    )

    password = models.CharField(
        max_length=30,
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    profile_picture = models.URLField(
        blank=True,
        null=True
    )


class Game(models.Model):
    title = models.CharField(
        max_length=30,
        unique=True,
    )

    category = models.CharField(
        max_length=15,
        choices=(
            ('Action', 'Action'),
            ('Adventure', 'Adventure'),
            ('Puzzle', 'Puzzle'),
            ('Strategy', 'Strategy'),
            ('Sports', 'Sports'),
            ('Board/Card Game', 'Board/Card Game'),
            ('Other', 'Other'),
        )
    )

    rating = models.FloatField(
        validators=(MinValueValidator(0.1),
                    MaxValueValidator(5.0),)
    )

    max_level = models.PositiveIntegerField(
        validators=(MinValueValidator(1),)
    )

    image_url = models.URLField()

    summary = models.TextField(
        blank=True,
        null=True
    )