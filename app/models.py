from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='children')
    is_visible = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title
