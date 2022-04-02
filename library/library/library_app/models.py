from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        verbose_name='First Name',
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name='Last Name',
    )
    image_url = models.URLField(
        verbose_name='Image URL',
    )


class Book(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='Title',

    )
    description = models.TextField(
        verbose_name='Description',
    )
    image = models.URLField(
        verbose_name='Image',
    )
    type = models.CharField(
        max_length=30,
        verbose_name='Type',
    )


