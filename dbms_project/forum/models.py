from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from users.models import CustomUser

# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField(max_length=25)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_text = models.CharField(max_length=500)
    post_timestamp = models.DateTimeField(default=timezone.now)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.post_title


class Reply(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=500)
    reply_timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reply_text
