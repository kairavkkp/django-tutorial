from django.db import models
from django.urls import reverse
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def get_absolute_path(self):
        return reverse('articles:article_list', kwargs={'id': self.id})
