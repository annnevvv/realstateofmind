from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from taggit.managers import TaggableManager

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLIC)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLIC = 'PB', 'Public'

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_post')
    tags=TaggableManager()
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publictiondate')
    content = models.TextField(max_length=3000)
    publictiondate = models.DateTimeField(default=timezone.now)
    creationeddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=1)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    object = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['publictiondate']
        indexes = [models.Index(fields=['publictiondate'])]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post-detail",
                       args=[self.publictiondate.year,
                             self.publictiondate.month,
                             self.publictiondate.day, self.slug])


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    email = models.EmailField()
    cmnt_txt = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created']), ]

    def __str__(self):
        return f"Comment from {self.email} for post '{self.post.title}'"
