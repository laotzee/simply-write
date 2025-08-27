from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    """Models different categories for prompts"""
    name = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0)

    def count(self):
        """Returns the amount of clicks the tag has received"""
        return self.click_count

    def increase_count(self):
        """Increases the amount of clicks the tag has received by 1"""
        self.click_count += 1
        self.save()
        return self

    def get_prompts(self):
        """Returns a QuerySet object with Prompt instances associated with the tag"""
        return self.prompts.all()

    def __str__(self):
        """Returns the name of the tag"""
        return self.name

class Prompt(models.Model):
    """Models writing prompts properties"""
    body = models.CharField(max_length=512)
    tag = models.ManyToManyField(Tag, related_name='prompts')
    likes = models.ManyToManyField(User, related_name='liked_prompts')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Returns the body of the prompt"""
        return self.body

    def like_list(self):
        """Returns a QuerySet of User instances who liked the prompt"""
        return self.likes.all()

    def like_count(self):
        """Returns the total amount of people who liked the prompt"""
        return len(self.like_list())

    def tags(self):
        """Returns a QuerySet of Tag instances associated with the prompt"""
        return self.tag.all()