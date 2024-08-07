from django import forms
from django.contrib.auth.models import User

class Registration(forms.Form):
    username = forms.CharField(max_length=50,required=True,error_messages={'required':'Please provide username'})
    email = forms.EmailField(max_length=250,required=True,error_messages={'required':'Please provide email'})
    password = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username','email','password']


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email Already used')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username Already used, try to use another')
        return username
    
class Userlogin(forms.Form):
    username = forms.CharField(max_length=50,required=True,error_messages={'required':'Please provide username'})
    password = forms.CharField(max_length=50,required=True,error_messages={'required':'Please provide password'})

    def clean_username(self):
        username = self.cleaned_data['username']
        if '@' in username:
            try:
                user = User.objects.get(email=username)
                return user.username
            except User.DoesNotExist:
                raise forms.ValidationError('Invalid Email Address')
        return username

class ProfileUpdate(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
