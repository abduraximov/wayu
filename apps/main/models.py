from django.db import models
from apps.common.models import BaseModel


class AboutUs(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    requirements = models.TextField()

    def __str__(self):
        return self.title


class Position(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Management(BaseModel):
    full_name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to="apps/main/photos", null=True, blank=True)
    days_admission = models.CharField()
    position = models.ForeignKey("main.Position", on_delete=models.CASCADE, related_name="position")
    phone_number = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField(max_length=64)
    biography = models.TextField()
    tasks = models.TextField()
    work_from = models.DateField()
    work_to = models.DateField()

    def __str__(self):
        return self.full_name


class Branch(models.Model):
    name = models.CharField(max_length=32)
    delegate = models.ForeignKey("main.Delegate", on_delete=models.CASCADE, related_name="delegate")
    location = models.CharField()

    def __str__(self):
        return self.name


class Vacancy(BaseModel):
    position = models.ForeignKey("main.Position", on_delete=models.CASCADE, related_name="position")
    location = models.CharField()
    requirements = models.TextField()
    salary = models.IntegerField(max_length=128)
    rate = models.IntegerField()

    def __str__(self):
        return self.position


class Resume(BaseModel):
    full_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    file = models.FileField(upload_to="apps/main/resumes")

    def __str__(self):
        return self.full_name


class Document(BaseModel):
    name = models.CharField(max_length=32)
    file = models.FileField(upload_to="apps/main/documents", null=True, blank=True)


class Project(models.Model):
    name = models.CharField()
    desc = models.CharField()
    photo = models.ImageField(upload_to="apps/main/photo_project", null=True, blank=True)
    our_goals = models.TextField()
    documents = models.ForeignKey("main.Document", on_delete=models.CASCADE, related_name="document")
    project_member = models.ForeignKey("main.Management", on_delete=models.CASCADE, related_name="project_members")


class Comment(BaseModel):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    text = models.TextField()
    project = models.ForeignKey("main.Project", on_delete=models.CASCADE, related_name="project")