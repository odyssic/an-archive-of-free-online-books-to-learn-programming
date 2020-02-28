from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    authors = models.ManyToManyField('Author')
    #Book.author_set.all()
    external_link = models.URLField
    published_date = models.DateField()
    write_up = models.TextField()
    # cover_art = models.ImageField()
    # thumbnail = models.ImageField()
    subjects = models.ManyToManyField('Subject')
    #Book.subject_set.all()

    def __str__(self):
        return f'{self.title}'

class Subject(models.Model):
    related_titles = models.ManyToManyField('Book')
    #you can find it with  Subject.book_set.all()

class Author(models.Model):
    works = models.ManyToManyField('Book')
    #Author.book_set.all()