from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully registered {username}.')
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})
