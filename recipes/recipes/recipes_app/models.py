from django.core.exceptions import ValidationError
from django.db import models
from re import compile

pattern = compile(r"^(\w+)(,\s\w+)$")


def validate_ingredients(input_string):
    if pattern.match(input_string) is None:
        raise ValidationError('The ingredients should be separated by ", "!')


class Recipe(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='Title'
    )
    image_url = models.URLField(
        verbose_name='Image URL',
    )
    description = models.TextField(
        verbose_name='Description',
    )
    ingredients = models.CharField(
        max_length=250,
        verbose_name='Ingredients',
        validators=(validate_ingredients,)
    )
    time = models.IntegerField(
        verbose_name='Time (Minutes)',
    )
