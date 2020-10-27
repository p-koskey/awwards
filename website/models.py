from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    fullname = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    profile_picture = CloudinaryField('image')

    def __str__(self):
        return f'{self.user.username} Account'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Post(models.Model):
    projectname = models.CharField(max_length=155)
    link = models.CharField(max_length=255)
    projectinfo = models.CharField(max_length=255)
    languages = models.CharField(max_length=200)
    picture = CloudinaryField('image')
    posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    
    def __str__(self):
        return str(self.projectname) if self.projectname else ''

class Rate(models.Model):
    design = models.CharField(max_length=30)
    usability = models.CharField(max_length=8)
    creativity = models.CharField(max_length=8,blank=True,null=True)
    average = models.FloatField(max_length=8)
    user = models.ForeignKey(User,null = True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='rate',null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.design
