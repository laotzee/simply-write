from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    """
    Models different categories for content
    """
    name = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Prompt(models.Model):
    """
    Models writing prompts properties
    """
    body = models.CharField(max_length=50)
    tag = models.ManyToManyField(Tag, related_name='tags')
    likes = models.ManyToManyField(User, related_name='liked_prompts')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body