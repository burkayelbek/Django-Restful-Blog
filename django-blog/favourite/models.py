from django.db import models
from django.contrib.auth.models import User
from post.models import Post


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    content = models.TextField()
