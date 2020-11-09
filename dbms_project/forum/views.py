from django.shortcuts import render
from django.views.defaults import page_not_found

# Create your views here.


def homePage(request):
    return render(request, 'forum/index.html')


def profilePage(request, usr_name):
    print(usr_name)
    # fetch user with the username variable and display that to user
    return render(request, 'forum/profile.html')


def profileAboutPage(request, usr_name):
    print(usr_name)
    # fetch user with the username variable and display that to user
    return render(request, 'forum/about.html')


def postPage(request, post_id):
    print(post_id)
    # fetch post with the post_id variable and display that to user
    return render(request, 'forum/post.html')


def searchResults(request, query):
    print(query)
    # do some searching using query string, and send that to the template
    return render(request, 'forum/search.html')


def faqPage(request):
    return render(request, 'forum/faq.html')


def notFoundPage(request, exception):
    return render(request, 'forum/404.html')
