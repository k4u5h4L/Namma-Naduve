from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages

from .models import Post, Reply, Tag, CustomUser
from .filters import PostFilter

from .forms import PostForm, ReplyForm


# Create your views here.

@login_required
def home_page(request):

    form = PostForm()

    posts = Post.objects.all().order_by('-post_timestamp')
    posts_count = posts.count()

    context = {
        'posts_count': posts_count,
        'form': form,
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
    try:
        user_page = CustomUser.objects.get(username=usr_name)
    except CustomUser.DoesNotExist:
        raise Http404("No CustomUser matches the given query.")

    posts = Post.objects.filter(author=user_page)
    # print(posts)

    context = {
        'user_page': user_page,
        # 'user_posts': posts,
    }

    replies = []
    context['posts'] = []

    for post in posts:
        replies.append(post.reply_set.all()[:2])

    posts = [post for post in posts]
    for i in range(len(posts)):
        context['posts'].append(
            {'post': posts[i], 'replies': replies[i]})

    # fetch user with the username variable and display that to user

    user_posts_count = Post.objects.filter(author=request.user).count()
    user_replies_count = Reply.objects.filter(author=request.user).count()

    context['user_posts_count'] = user_posts_count
    context['user_replies_count'] = user_replies_count

    print(context)

    return render(request, 'forum/profile.html', context)


@login_required
def profile_about_page(request, usr_name):
    print(usr_name)
    # fetch user with the username variable and display that to user
    return render(request, 'forum/about.html', context)


@login_required
def post_page(request, post_id):
    # print(post_id)
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

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


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.tags = form.cleaned_data.get('tags')
            print(post.tags)
            post.save()

            post_title = form.cleaned_data.get('post_title')
            print(f'Post just posted successfully: {post_title}!')
            messages.success(request, f'Your post was posted successfully')

        else:
            # print("Form wasn't valid")
            messages.error(
                request, f'Form is not validated')

        return redirect('home_page')
    else:
        # print("A GET req was made")
        return redirect('home_page')


@login_required
def create_reply(request):
    if request.method == "POST":
        form = ReplyForm(request.POST)

        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.save()

            reply_text = form.cleaned_data.get('reply_text')
            print(f'Reply just saved successfully: {reply_text}!')
            messages.success(request, f'Your reply was posted successfully')

        else:
            # print("Form wasn't valid")
            messages.error(
                request, f'Form is not validated')

        return redirect('home_page')
    else:
        # print("A GET req was made")
        return redirect('home_page')


def faq_page(request):
    return render(request, 'forum/faq.html')


def not_found_page(request, exception):
    return render(request, 'forum/404.html')
