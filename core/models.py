from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image


class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL, null=True,)
    external_link = models.URLField()
    published_date = models.DateField()
    write_up = models.TextField()
    subject = models.ForeignKey(
        'Subject',
        on_delete=models.SET_NULL, null=True,)
    image = models.FileField(
        upload_to='images', null=True, verbose_name=None)

    def __str__(self):
        return f'{self.title}'


class Subject(models.Model):

    genre = models.CharField(max_length=20)
    about = models.TextField()
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.genre}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.genre)
        return super().save(*args, **kwargs)


class Author(models.Model):
    name = models.CharField(max_length=40)
    about = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Favorite(models.Model):

    person = models.ForeignKey(
        User, related_name="favorites", on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, related_name="favorites", on_delete=models.CASCADE)

    def __str__(self):
        return f'Person: {self.person}, Book: {self.book}'
