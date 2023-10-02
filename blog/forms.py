from django import forms

from blog.models import PostComment


class EmailPostForm(forms.Form):
    sender_name = forms.CharField(max_length=30)
    sender_email = forms.EmailField()
    recipient_email = forms.EmailField()
    message = forms.CharField(required=False, widget=forms.Textarea)


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['email', 'email', 'cmnt_txt']
