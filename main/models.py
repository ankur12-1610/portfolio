from django.db import models
from django.urls import reverse

# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=400)
    tutorial_content = models.TextField()

    def __str__(self):
        return self.tutorial_title  

