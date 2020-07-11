from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField('text')
    author = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"