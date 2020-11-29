from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.conf import settings
from django.views.defaults import page_not_found
from django.views.defaults import server_error

import os

from .models import Post, Reply, Tag, CustomUser
from .filters import PostFilter

from .forms import PostForm, ReplyForm, ProfileUpdateForm, ProfilePicUpdateForm

from .neural_net.toxicity import is_toxic
 

# Create your views here.

@login_required
def home_page(request):
    name=request.user

    post_form = PostForm()
    reply_form = ReplyForm()

    posts = Post.objects.all().order_by('-post_timestamp')

    paginate = Paginator(posts, 5)
    # the paginator object takes in the full posts query, and the amount of posts per page

    page_num = request.GET.get('page', 1)

    try:
        page = paginate.page(page_num)
    except EmptyPage:
        page = paginate.page(1)

    posts = page
    # print(posts.has_next)

    # posts_count = posts.count()

    context = {
        # 'posts_count': posts_count,
        'post_form': post_form,
        'reply_form': reply_form,
        'page_obj': page,
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
    post_form = PostForm()
    reply_form = ReplyForm()
    # print(posts)

    context = {
        'user_page': user_page,
        'post_form': post_form,
        'reply_form': reply_form,
        'username': usr_name,
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

    # print(context)

    return render(request, 'forum/profile.html', context)


@login_required
def delete_post(request,post_id=None):
    val=None
    user=request.user
    Post.objects.filter(id=post_id).delete()
    # post_to_delete=Post.objects.get(id=post_id)
    # print(post_to_delete)
    # post_to_delete.delete()
    return redirect('profile_page',user)


@login_required
def profile_about_page(request, usr_name):
    val=None
    # print(usr_name)
    try:
        user_page = CustomUser.objects.get(username=usr_name)
    except CustomUser.DoesNotExist:
        raise Http404("No CustomUser matches the given query.")

    user_posts_count = Post.objects.filter(author=request.user).count()
    user_replies_count = Reply.objects.filter(author=request.user).count()

    context = {
        'user_page': user_page,
        'user_replies_count': user_replies_count,
        'user_posts_count': user_posts_count,
    }
    # fetch user with the username variable and display that to user
    return render(request, 'forum/about.html', context)

@login_required
def profile_update_page(request, usr_name):
    if request.method == 'POST':
        profile = request.user.profile
        u_form = ProfileUpdateForm(request.POST, instance=profile)
        t_or_s = request.POST['radio']

        if u_form.is_valid():
            # u_form.save()
            profile_update_form_submitted = u_form.save(commit=False)
            profile_update_form_submitted.t_s = t_or_s
            profile_update_form_submitted.save()
            
            print(f'Your account has been Updated')
            messages.success(request, f'Your account has been Updated')
            return redirect('profile_about_page', usr_name)
        else:
            print("Form was not validated")
            return redirect('profile_about_page', usr_name)
    else:
        try:
            user_page = CustomUser.objects.get(username=usr_name)
        except CustomUser.DoesNotExist:
            raise Http404("No CustomUser matches the given query.")

        profile_update_form = ProfileUpdateForm()
        
        user_posts_count = Post.objects.filter(author=request.user).count()
        user_replies_count = Reply.objects.filter(author=request.user).count()

        context = {
            'user_page': user_page,
            'profile_update_form': profile_update_form,
            'user_replies_count': user_replies_count,
            'user_posts_count': user_posts_count,
        }
        return render (request, 'forum/update_profile.html', context)

@login_required
def profile_picture_page(request, usr_name):
    if request.method == 'POST':
        # removes the old profile pic before updating the new one
        if request.user.profile.image.url != '/media/default.png':
            os.remove(f'{settings.BASE_DIR}/{request.user.profile.image.url}')
            print(f'Old profile pic has been deleted')
        else:
            print(f'Updating pic for first time')

        pic_form = ProfilePicUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if pic_form.is_valid():
            # print(request.user.profile.image.url)
            pic_form.save()
            print(f'Your profile pic has been Updated')
            messages.success(request, f'Your Profile Picture has been Updated')
            return redirect('profile_about_page', usr_name)
        else:
            print("Form was not validated")
            return redirect('profile_about_page', usr_name)
    else:
        return redirect('profile_about_page', usr_name)
        
@login_required
def post_page(request, post_id):
    val=None
    # print(post_id)
    reply_form = ReplyForm()

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("No Post matches the given query.")

    replies = post.reply_set.all()
    tags = post.tags.all()

    context = {
        'post': post,
        'replies': replies,
        'tags': tags,
        'reply_form':reply_form,
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
        # print(request.POST)
        # print(request.user)
        form = PostForm(request.POST)

        if form.is_valid():
            post_title = form.cleaned_data.get('post_title')
            post_text= form.cleaned_data.get('post_text')

            if_toxic = is_toxic([post_title, post_text])

            if 1.0 in if_toxic:
                print(f'User post title or post text has toxic content') 
                messages.error(request, f'Your post title or post text might have toxic content. We request you to change them in order to post.')
                return redirect('home_page')

            post = form.save(commit=False)
            post.author = request.user
            form.save()
            print(f'Post just posted successfully: {post_title}!')
            messages.success(request, f'Your post was posted successfully')

        else:
            print("Form wasn't valid")
            messages.error(
                request, f'Form is not validated')

        return redirect('home_page')
    else:
        print("A GET req was made")
        return redirect('home_page')


@login_required
def create_reply(request, post_id):
    
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("No Post matches the given query.")

    if request.method == "POST":
        form = ReplyForm(request.POST)

        if form.is_valid():
            reply_text = form.cleaned_data.get('reply_text')

            if_toxic = is_toxic([reply_text])

            if 1.0 in if_toxic:
                print(f'User reply text has toxic content') 
                messages.error(request, f'Your reply text might have toxic content. We request you to change them in order to post.')
                return redirect('home_page')

            reply = form.save(commit=False)
            reply.author = request.user
            reply.parent_post = post
            reply.save()

            print(f'Reply just saved successfully: {reply_text}!')
            messages.success(request, f'Your reply was posted successfully')

        else:
            # print("Form wasn't valid")
            messages.error(
                request, f'Form is not validated')

        return redirect('post_page',post_id)
    else:
        # print("A GET req was made")
        return redirect('home_page')


def faq_page(request):
    return render(request, 'forum/faq.html')


def not_found_page(request, exception):
    return render(request, 'forum/404.html')

def not_found_page_server(request):
    return render(request, 'forum/404.html')