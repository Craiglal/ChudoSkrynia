from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=40, label='Ім''я')
    sender = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Повідомлення')
    copy = forms.BooleanField(required=False, label='Відправити копію для себе')
