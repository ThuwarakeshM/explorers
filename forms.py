from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()