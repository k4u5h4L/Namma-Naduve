from django.shortcuts import render
from django.views.defaults import page_not_found

# Create your views here.


def homePage(request):
    return render(request, 'forum/index.html')


def faqPage(request):
    return render(request, 'forum/faq.html')


def searchResults(request, query):
    print(query)
    return render(request, 'forum/search.html')


def notFoundPage(request, exception):
    return render(request, 'forum/404.html')
