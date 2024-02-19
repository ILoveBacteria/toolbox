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


class Footprint(models.Model):
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField()

    def __str__(self):
        return self.title


class LeetcodeTopic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Leetcode(models.Model):
    class Beauty(models.IntegerChoices):
        BAD = 1
        REVIEW_IF_HAVE_TIME = 2
        GOOD_FOR_REVIEW = 3
        VERY_INSIGHTFUL_IDEA = 4

    name = models.CharField(max_length=255)
    problem_beauty = models.IntegerField(choices=Beauty.choices)
    topics = models.ManyToManyField(LeetcodeTopic)
    url = models.URLField()
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
