from django import forms

class signUp(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control m-input border border-dark validateInput', 'placeholder': 'First Name'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control m-input border border-dark validateInput', 'placeholder': 'Last Name'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control m-input border border-dark validateInput', 'placeholder': 'User Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control m-input  border-dark validateInput', 'placeholder': 'Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control m-input border border-dark validateInput', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control m-input border border-dark validateInput', 'placeholder': 'Confirm Password'}))

class loginform(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control m-input', 'placeholder': 'Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control m-input', 'placeholder': 'Password'}))