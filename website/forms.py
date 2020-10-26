from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from .models import Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class PostForm(forms.ModelForm):
    picture = CloudinaryField('image')

    class Meta:
        model = Post
        fields = ('picture', 'projectname', 'link', 'projectinfo', 'languages',) 