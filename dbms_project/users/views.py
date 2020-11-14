from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.

# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'forum/signup.html'


def landing_page(request):
    form = CustomUserCreationForm()

    context = {'form': form}

    return render(request, 'users/landing.html', context)


def login(request):
    if request.method == "POST":
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home_page')
        else:
            messages.error(
                request, f'Username or password incorrect')

    return redirect('landing_page')


def logout(request):
    auth_logout(request)
    return redirect('landing_page')


def register(request):
    if request.method == "POST":
        print(request.POST)
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            print(f'Account created for {username}!')

            return redirect('home_page')
        else:
            messages.error(
                request, f'The data you have filled seems to be incorrect, or there may already be a user with that username')

            return redirect('landing_page')

    return redirect('home_page')
