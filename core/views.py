from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_list_or_404, render, redirect
from .models import Book, Author, Subject, Image, User, Favorite
from django.contrib.auth.decorators import login_required


@login_required
def homepage(request):
    books = Book.objects.all()
    favorite_books = get_favorites_for_user(request)
    return render(request, 'core/index.html', {'books': books, 'favorites': favorites})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'core/book-detail.html', {'book': book, 'pk': pk})


def author(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'core/author.html', {'author': author, 'pk': pk})


def subject(request, pk):
    subject = Subject.objects.get(pk=pk)
    return render(request, 'core/subject.html', {'subject': subject, 'pk': pk})


def books_by_subject(request, slug):
    book = Book.objects.get(slug=slug)
    books_for_subject = Book.objects.filter(subject=subject)
    return render(request, 'core/books_for_subject.html', {'books': books_for_subject, 'subject': subject})


def get_favorites_for_user(request):
    user = User.objects.get(username=request.user.username)
    favorite_books = [favorite.book for favorite in user.favorites.all()]
    return favorite_books
