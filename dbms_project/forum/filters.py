import django_filters
from django_filters import CharFilter

from forum.models import *


class PostFilter(django_filters.FilterSet):
    post_title = CharFilter(field_name='post_title', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = '__all__'
