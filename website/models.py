from django.db import models


class Education(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)

    def __str__(self):
        return self.title
