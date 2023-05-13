from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='posts',
    )

    def __str__(self):
        return f'{self.title.title()[:15]} : {self.description[:30]}'


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name.title()


