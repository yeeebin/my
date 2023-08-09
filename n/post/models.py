from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='post/', default='default.png')
    likes = models.ManyToManyField(User)
    tag = models.ManyToManyField()
    published_date = models.DateTimeField(default=timezone.now)


class Tag(models.model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Reply(models.Model):
    reply = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    Comment = models.ForeignKey(Comment, on_delete=models.CASCADE)