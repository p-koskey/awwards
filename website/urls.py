from django.urls import path,include
from django.contrib.auth.views import LogoutView
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', views.register, name='register'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/edit', views.edit_profile, name='edit'),
    path('details/<post_id>/', views.postdetail, name='details'),
    path('search/',views.search_results, name='search_results')
]