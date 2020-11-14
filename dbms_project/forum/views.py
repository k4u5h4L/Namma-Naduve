from django.shortcuts import render
from django.views.defaults import page_not_found
from .models import Post, Reply, Tag, CustomUser

# Create your views here.


def home_page(request):

    context = {
        'posts': Post.objects.all().order_by('-post_timestamp'),
        'replies': Reply.objects.all(),
    }

    # print(context)
    return render(request, 'forum/index.html', context)


def profile_page(request, usr_name):
    print(usr_name)
    # fetch user with the username variable and display that to user
    return render(request, 'forum/profile.html')


def profile_about_page(request, usr_name):
    print(usr_name)
    # fetch user with the username variable and display that to user
    return render(request, 'forum/about.html')


def post_page(request, post_id):
    # print(post_id)
    post = Post.objects.get(id=post_id)
    replies = post.reply_set.all()
    tags = post.tags.all()
    context = {
        'post': post,
        'replies': replies,
        'tags': tags,
    }
    print(context)
    # fetch post with the post_id variable and display that to user
    return render(request, 'forum/post.html', context)


def search_results(request, query):
    print(query)
    # do some searching using query string, and send that to the template
    return render(request, 'forum/search.html')


def faq_page(request):
    return render(request, 'forum/faq.html')


def not_found_page(request, exception):
    return render(request, 'forum/404.html')
