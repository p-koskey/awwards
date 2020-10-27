from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from .models import Post, Profile, Rate

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

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fullname', 'location', 'profile_picture', 'bio']

class RateForm(forms.ModelForm):
    design = forms.ChoiceField(choices=[(x, x) for x in range(0, 11)])
    usability = forms.ChoiceField(choices=[(x, x) for x in range(0, 11)])
    content = forms.ChoiceField(choices=[(x, x) for x in range(0, 11)])
    class Meta:
        model =Rate
        fields= ['design','usability','content']
        