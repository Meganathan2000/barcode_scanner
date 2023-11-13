from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import data  # Import your custom form

def register(request):
    if request.method == 'POST':
        form = data(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your desired page

    else:
        form = data()

    return render(request, 'registration/register.html', {'form': form})

