from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


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
    featured_image = CloudinaryField('image', default='placeholder')
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    APPROVAL = ((0, "Pending Approval"), (1, "Approved"))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.author}"
