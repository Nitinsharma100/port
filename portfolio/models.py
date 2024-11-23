from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return self.name



