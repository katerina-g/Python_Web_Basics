from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        verbose_name='First Name',
    )
    last_name = models.CharField(
        max_length=20,
        verbose_name='Last Name',
    )
    age = models.IntegerField(
        verbose_name='Age',
    )
    image_url = models.URLField(
        verbose_name='Link to Profile Image',
    )


class Note(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='Title',
    )
    image_url = models.URLField(
        verbose_name='Link to Image',
    )
    content = models.TextField(
        verbose_name='Content',
    )