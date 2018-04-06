from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Article(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    pub_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True,null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']
        verbose_name = '文章'
        verbose_name_plural = '文章'
