from django.db import models


class Task(models.Model):
    title = models.CharField(
        max_length=25,
    )
    text = models.TextField(
        max_length=150,
    )

    def __str__(self):
        return f'{self.id}: {self.title}'
