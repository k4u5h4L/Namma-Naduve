from django.shortcuts import render
from django.views.defaults import page_not_found 

# Create your views here.

def homePage(request):
    return render(request, 'forum/index.html')

def faqPage(request):
    return render(request, 'forum/faq.html')
