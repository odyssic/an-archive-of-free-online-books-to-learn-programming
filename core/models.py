from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    authors = models.ManyToManyField('Author')
    external_link = models.URLField
    published_date = models.DateField()
    write_up = models.TextField()
    # cover_art = models.ImageField()
    # thumbnail = models.ImageField()
    subjects = models.ManyToManyField('Subject')

    def __str__(self):
        return f'{self.title}'

class Subject(models.Model):
    related_titles = models.ManyToManyField('Book')

class Author(models.Model):
    works = models.ManyToManyField('Book')