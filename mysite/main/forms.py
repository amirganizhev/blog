from django import forms


class Comment(forms.Form):
    body = forms.CharField(widget=forms.Textarea)
