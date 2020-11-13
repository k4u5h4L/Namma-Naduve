from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'forum/signup.html'


def landing_page(request):
    form = UserCreationForm()

    context = {'form': form}

    return render(request, 'users/landing.html', context)
