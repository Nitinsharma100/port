from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)  # Project name
    description = models.TextField()  # Short description
    image = models.ImageField(upload_to='projects', blank=True, null=True)  # Project image
    github_link = models.URLField()  # GitHub source code link
    section = models.CharField(max_length=30, blank=True, null=True)  # Section/category of the project
    timestamp = models.DateTimeField(auto_now_add=True)  # When the project was added

    def __str__(self):
        return self.name


