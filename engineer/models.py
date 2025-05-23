from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    streak = models.IntegerField(default=0)
    last_seen = models.DateField(null=True, blank=True)
    total_known = models.IntegerField(default=0)

    def update_streak(self):
        today = date.today()
        if self.last_seen != today:
            if self.last_seen == today - timedelta(days=1):
                self.streak += 1
            else:
                self.streak = 1
            self.last_seen = today
            self.save()

    def reset_streak(self):
        self.streak = 0
        self.save()



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
    

class Vocabulary(models.Model):
    word = models.CharField(max_length=255, unique=True)
    seen = models.PositiveIntegerField(default=1)
    know = models.PositiveIntegerField(default=0)
    translation = models.TextField(blank=True)
    example = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def know_rate(self):
        return f'{self.know * 100 / self.seen:.1f}%'

    def __str__(self) -> str:
        return self.word
