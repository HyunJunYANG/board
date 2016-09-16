from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content','photo')
        widgets={'title':forms.TextInput(attrs={'size':20}),
            'content':forms.Textarea(attrs={'rows':5, 'cols':15}),}
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('author', 'message')
