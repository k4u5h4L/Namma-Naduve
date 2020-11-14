import django_filters
from django_filters import DateFilter

from .models import *


class PostFilter(django_filters.FilterSet):

    class Meta:
        model = Post
        fields = '__all__'
