from django.contrib import admin
from .models import Book, Subject, Author, Favorite

admin.site.register(Book)
admin.site.register(Subject)
admin.site.register(Author)
admin.site.register(Favorite)
