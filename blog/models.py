from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    excerpt = models.TextField(blank=True)
    test_content = RichTextField(blank=True, config_name='default')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)


class Comment(models.Model):
    APPROVAL = ((0, "Pending Approval"), (1, "Approved"))
    author = models.ForeignKey(User, on_delete=models.CASADE, related_name="user_comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(choices=APPROVAL, default=0)
    created_on = models.DateTimeField(auto_add_on=True)
