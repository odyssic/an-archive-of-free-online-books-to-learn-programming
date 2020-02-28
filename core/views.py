
from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import get_list_or_404, render, redirect

from .models import Book, Author, Subject


def homepage(request):
    books = Book.objects.all()

    return render(request, 'core/index.html', {'books': books})
