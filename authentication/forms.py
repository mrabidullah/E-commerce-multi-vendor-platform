from django import forms 
import re


class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    image = forms.ImageField(required=False)

    def clean_username(self):
        username = self.cleaned_data.get("username")

        
        if not re.match(r'^[A-Za-z]+$', username):
            raise forms.ValidationError(
                "Username must contain only letters (A-Z). No numbers or symbols allowed."
            )

        return username

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)