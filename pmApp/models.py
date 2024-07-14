from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class MyPasswords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pass_word = models.CharField(max_length=225, blank=True)
    
    def __str__(self):
        return self.user