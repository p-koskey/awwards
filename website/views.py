from django.http  import HttpResponse
from django.shortcuts import render, redirect
from django.http  import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, PostForm,UpdateUserForm,UpdateProfileForm, RateForm
from .models import Post,Profile, User,Rate
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProfileSerializer, UserSerializer, PostSerializer
import random
# Create your views here.


def welcome(request):
    try:
    posts = Post.objects.all().order_by("-posted")
    rpost = random.randint(0, len(posts)-1)
    randompost = posts[rpost]
    except Post.DoesNotExist:
        posts = None
    if request.method == 'POST':
        uform = PostForm(request.POST, request.FILES)
        if uform.is_valid():
            post = uform.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        uform = PostForm()
    return render(request, 'index.html',{'uform': uform,'posts':posts,'randompost':randompost})
    

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

@login_required(login_url='login')
def profile(request, username):
    return render(request, 'profile.html')


@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'editprofile.html', params)
@login_required(login_url='login')
def postdetail(request,post_id):

    post= Post.objects.get(pk=post_id)
    ratings = Rate.objects.filter(post_id=post_id)
    design = Rate.objects.filter(post_id=post_id).values_list('design',flat=True)
    usability = Rate.objects.filter(post_id=post_id).values_list('usability',flat=True)
    content = Rate.objects.filter(post_id=post_id).values_list('content',flat=True)
    total_design=0
    total_usability=0
    total_content = 0
    print(design)
    for rate in design:
        total_design+=rate
    print(total_design)

    for rate in usability:
        total_usability+=rate
    print(total_usability)

    
    for rate in content:
        total_content+=rate
    print(total_content)

    total=(total_design+total_content+total_usability)/3


    post.design = total_design
    post.usability = total_usability
    post.content = total_content
    post.total = total

    post.save()


    if request.method =='POST':
        form = RateForm(request.POST,request.FILES)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.post= post
            rate.user = request.user
            rate.total = (rate.design+rate.usability+rate.content)/2
            rate.save()
    else:
        form = RateForm()

       
    return render(request,"postdetail.html", {'post':post,"ratings":ratings, 'form':form,})
@login_required(login_url='/accounts/login/')
def search_results(request):
    current_user = request.user
    post =Post.objects.get(user=current_user)
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_post(search_term)
        message=f"{search_term}"

        return render(request,'search.html',{"message":message,"posts":searched_posts,"post":post})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer