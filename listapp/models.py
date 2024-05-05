from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=False, max_length=200)

    def __str__(self):
        return self.title


class Item(models.Model):
    name = models.CharField(blank=False, max_length=200)
    slug = models.SlugField(blank=False, max_length=200)
    complete = models.BooleanField(default=False)
    list_name = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name="items")

    class Meta:
        ordering = ['-complete']

    def __str__(self):
        return self.name
