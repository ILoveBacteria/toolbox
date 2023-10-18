from django.core.validators import RegexValidator
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Term(models.Model):
    name = models.CharField(max_length=255, unique=True)
    page = models.PositiveIntegerField()
    description = models.TextField(blank=True, validators=(RegexValidator(r"^[\w.,:()-=+!/?|'\"{}: ]*$"),))
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
