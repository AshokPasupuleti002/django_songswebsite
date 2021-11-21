from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Enter name', required=True)
    contact_email = forms.EmailField(label='Enter email id', required=True)
    content = forms.CharField(label='Content', required=True, widget=forms.Textarea, max_length=1500)


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
