from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Term(models.Model):
    name = models.CharField(max_length=255)
    page = models.PositiveIntegerField()
    description = models.TextField(null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
