from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    userpassword = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(LoginForm):
    # username = forms.CharField(max_length=20)
    # userpassword = forms.CharField(widget=forms.PasswordInput)
    useremail = forms.EmailField(max_length=40, required=False)
