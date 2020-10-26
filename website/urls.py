from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('register/', views.register, name='register'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/edit', views.edit_profile, name='edit'),
]