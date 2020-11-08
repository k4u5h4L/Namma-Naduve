from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def landingPage(request):
    form = UserCreationForm()

    context = {'form': form}

    return render(request, 'users/landing.html', context)
