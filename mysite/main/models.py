from django.db import models


class NewsPages(models.Model):
    name = models.CharField(max_length=120)
    body = models.TextField()
    image = models.ImageField()
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_create']
