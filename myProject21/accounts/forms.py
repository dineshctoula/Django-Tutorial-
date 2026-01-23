from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    


    class Meta:
        model=User
        fields=['username','email','password1','password2']
    def clean_email(self):
        # yesle chae email lai validate garxa
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("email already exist")
        return email
