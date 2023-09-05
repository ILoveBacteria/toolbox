from django.db import models


class Education(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)


class Experience(models.Model):
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)


class Certificate(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
