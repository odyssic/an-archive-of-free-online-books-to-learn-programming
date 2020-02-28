from django.db import models


class Book(models.Model):
    title = 'tbd'
    authors = 'tbd'
    external_link = 'tbd'
    published_date = 'tbd'
    write_up = 'tbd'
    cover_art = 'tbd'

    def __str__(self):
        return f'{self.title}'

class Category(models.Model):
    genre = ''
    associated_titles = []