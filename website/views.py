from django.http  import HttpResponse
from django.shortcuts import render, redirect
from django.http  import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, PostForm
from .models import Post,Profile, User
# Create your views here.

def welcome(request):
    posts = Post.objects.all()
    
    if request.method == 'POST':
        uform = PostForm(request.POST, request.FILES)
        if uform.is_valid():
            post = uform.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        uform = PostForm()
    return render(request, 'index.html',{'uform': uform,'posts':posts})
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('welcome')
    else:
        form = RegisterForm()
    return render(request, 'django_registration/registration_form.html', {'form': form})