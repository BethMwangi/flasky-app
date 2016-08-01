from django import forms
from .models import Post, Comment
# from django_markdown.fields import MarkdownField
# from django_markdown.widgets import MarkdownWidg

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


