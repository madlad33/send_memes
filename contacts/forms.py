from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_no']


class MessageForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
