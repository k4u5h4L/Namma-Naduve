from django.shortcuts import render
from django.views.defaults import page_not_found
from django.views.generic import DetailView,CreateView
from .models import Post, Reply, Tag, CustomUser

# Create your views here.


def home_page(request):
    context = {
        'posts': Post.objects.all().order_by('-post_timestamp'),
        'replies': Reply.objects.all().order_by('-reply_timestamp'),
    }
    
    
    return render(request, 'forum/index.html', context)



def profile_page(request, usr_name):
    print(usr_name)
    # fetch user with the username variable and display that to user
    return render(request, 'forum/profile.html')


def profile_about_page(request, usr_name):
    print(usr_name)
    # fetch user with the username variable and display that to user
    return render(request, 'forum/about.html')


class postview(DetailView):
    model = Post
    template_name = 'forum/post.html'
    context_object_name = 'posts'

# class postcreate(CreateView):
#     model = Post
#     fields = ['post_title','post_text']
#     template_name = 'forum/index.html'

#     def form_valid(self,form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
    
    # template_name = 'forum/post.html'
    # context_object_name = 'posts'
# def post_page(request, post_id):
#     print(post_id)
#     # fetch post with the post_id variable and display that to user
#     return render(request, 'forum/post.html')


def search_results(request, query):
    print(query)
    # do some searching using query string, and send that to the template
    return render(request, 'forum/search.html')


def faq_page(request):
    return render(request, 'forum/faq.html')


def not_found_page(request, exception):
    return render(request, 'forum/404.html')
