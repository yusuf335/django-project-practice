from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.TextField()
    number = models.JSONField(blank=True, null=True)
    

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.name

class ProfileJson(models.Model):
    profile_json = models.JSONField(blank = True, null=True)
    def __str__(self):
        return self.profile_json


