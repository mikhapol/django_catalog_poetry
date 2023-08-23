from django import forms

from app_blog.models import Blog
from app_catalog.forms import StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
