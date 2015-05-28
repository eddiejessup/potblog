from django import forms
from blog.models import Post, Comment


class CreatePostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ['title', 'date_published', 'text']


class CreateCommentForm(forms.ModelForm):
    author = forms.CharField(label='Name (required)')
    email = forms.CharField(label='Email (optional)')
    text = forms.CharField(widget=forms.Textarea, label='')

    class Meta:
        model = Comment
        fields = ['author', 'email', 'text']
