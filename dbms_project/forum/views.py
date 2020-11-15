from django.shortcuts import render
from django.views.defaults import page_not_found
from django.contrib.auth.decorators import login_required

from .models import Post, Reply, Tag, CustomUser
from .filters import PostFilter


# Create your views here.

@login_required
def home_page(request):

    posts = Post.objects.all().order_by('-post_timestamp')
    posts_count = posts.count()

    context = {
        'posts_count': posts_count,
    }

    replies = []
    context['posts'] = []

    for post in posts:
        replies.append(post.reply_set.all()[:2])

    posts = [post for post in posts]
    for i in range(len(posts)):
        context['posts'].append(
            {'post': posts[i], 'replies': replies[i]})

    # print(context)

    # print(request.user)

    user_posts_count = Post.objects.filter(author=request.user).count()
    user_replies_count = Reply.objects.filter(author=request.user).count()

    context['user_posts_count'] = user_posts_count
    context['user_replies_count'] = user_replies_count

    return render(request, 'forum/index.html', context)


@login_required
def profile_page(request, usr_name):
    print(usr_name)
    # fetch user with the username variable and display that to user
    return render(request, 'forum/profile.html')


@login_required
def profile_about_page(request, usr_name):
    print(usr_name)
    # fetch user with the username variable and display that to user
    return render(request, 'forum/about.html')


@login_required
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
    # print(context)
    return render(request, 'forum/post.html', context)


@login_required
def search_results(request):
    # print(query)

    posts = Post.objects.all()

    postFilter = PostFilter(request.GET, queryset=posts)

    posts = postFilter.qs

    context = {
        'postFilter': postFilter,
        'posts': posts,
    }
    # do some searching using query string, and send that to the template
    return render(request, 'forum/search.html', context)


def faq_page(request):
    return render(request, 'forum/faq.html')


def not_found_page(request, exception):
    return render(request, 'forum/404.html')
