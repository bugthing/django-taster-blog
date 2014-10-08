from django import forms
from blog.models import Posting

class PostingForm(forms.ModelForm):
    content = forms.CharField( widget=forms.Textarea, label='', required=True)
    class Meta:
        model = Posting
        exclude = ('date',)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', required=True)
