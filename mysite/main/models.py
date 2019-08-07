from django.db import models


# Create your models here.

class News_pages(models.Model):
    name = models.CharField(max_length=120)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name