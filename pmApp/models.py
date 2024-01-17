from django.db import models

class PasswordEntry(models.Model):
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

