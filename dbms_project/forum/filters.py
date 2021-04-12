import django_filters
from django_filters import CharFilter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from forum.models import *


class PostFilter(django_filters.FilterSet):
    post_title = CharFilter(field_name='post_title', lookup_expr='icontains')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('post_title', css_class='form-group col-md-6 mb-0'),
    #             # Column('tags', css_class='form-group col-md-6 mb-0'),
    #             # Column('author', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #     )    

    class Meta:
        model = Post
        fields = ['post_title', 'tags', 'author']
