from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

#abstracebaseuser
class User(AbstractUser):
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.email)


class Blog(models.Model):
    title=models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    title_slug=models.CharField(max_length=130)
    content=models.TextField()
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.title)
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    dateTime=models.DateTimeField(default=now)
 
    def __str__(self):
        return self.user.username +  " Comment: " + self.content