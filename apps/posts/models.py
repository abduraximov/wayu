from django.db import models
from apps.common.models import BaseModel


class Region(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=256)
    desc = models.CharField(max_length=512)
    text = models.TextField()
    photo = models.ImageField(upload_to="apps/posts/photos", null=True, blank=True)
    category = models.ForeignKey("posts.Category", on_delete=models.CASCADE, related_name="category")
    tags = models.ManyToManyField("posts.Tag", on_delete=models.CASCADE, related_name="tag")
    views = models.IntegerField()
    about_us = models.BooleanField(default=False)
    region = models.ForeignKey("posts.Region", on_delete=models.CASCADE, related_name="region")
