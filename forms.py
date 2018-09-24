from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
