from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_list_or_404, render, redirect
from .models import Book, Author, Subject, Image
from django.contrib.auth.decorators import login_required


@login_required
def homepage(request):
    books = Book.objects.all()
    # subjects = Subject.objects.all()
    # authors = Author.objects.all()
    # images = Image.objects.all()
    return render(request, 'core/index.html', {'books': books})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'core/book-detail.html', {'book': book, 'pk': pk})


def author(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'core/author.html', {'author': author, 'pk': pk})


def subject(request, pk):
    subject = Subject.objects.get(pk=pk)
    return render(request, 'core/subject.html', {'subject': subject, 'pk': pk})
