from .models import Post
from django import forms





class LoaderForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("image",)
