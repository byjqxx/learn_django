from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    userpassword = forms.CharField(widget=forms.PasswordInput)
    useremail = forms.EmailField()