from django.forms import ModelForm, Form
from .models import Post, Reply


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_text', 'tags']
        exclude = ['author']


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_text']
        exclude = ["author", "parent_post"]
