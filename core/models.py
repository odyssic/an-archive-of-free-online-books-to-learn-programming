from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image


class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey(
        'Author',
        on_delete=models.DO_NOTHING,)
    external_link = models.URLField()
    published_date = models.DateField()
    write_up = models.TextField()
    subject = models.ForeignKey(
        'Subject',
        on_delete=models.DO_NOTHING,)
    image = models.FileField(
        upload_to='images', null=True, verbose_name=None)

    def __str__(self):
        return f'{self.title}'


class Subject(models.Model):
    genre = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.genre}'


class Author(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'