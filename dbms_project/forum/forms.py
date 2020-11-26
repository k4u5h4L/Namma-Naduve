from django.forms import ModelForm, Form
from .models import Post, Reply
from users.models import Profile


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_text', 'tags']
        exclude = ['author']


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_text']
        exclude = ['author', 'parent_post']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile 
        fields = ['full_name','location','phone_no','personal_site', 'bio']

class ProfilePicUpdateForm(ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']