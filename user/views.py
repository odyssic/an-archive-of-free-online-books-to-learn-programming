from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def register(request):
    form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})
