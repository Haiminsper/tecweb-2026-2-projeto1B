from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
