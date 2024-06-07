from django.db import models

# Create your models here.

class MyPortfolio(models.Model):
    title = models. CharField(max_length= 150)
    description = models.TextField(max_length= 5000)
    link = models.URLField()

    def __str__(self) -> str:
        return self.title
