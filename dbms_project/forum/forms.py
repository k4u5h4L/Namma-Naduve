from django.forms import ModelForm, Form
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_text', 'tags']
        exclude = ["author"]
