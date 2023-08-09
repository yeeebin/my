from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    images = models.ImageField(upload_to='post/', default='default.png')
    likes = models.ManyToManyField(User, related_name='like_posts', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)




#class Tag(models.Model):
    #name = models.CharField(max_length=100)
    #post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')

    #def __str__(self):
        #return self.name
    

class Comment(models.Model):
    comment = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='like_posts', blank=True)

    def __str__(self):
        return self.comment


class Reply(models.Model):
    reply = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    Comment = models.ForeignKey(Comment, on_delete=models.CASCADE)