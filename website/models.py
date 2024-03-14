from django.db import models


class AbstractInfo(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    company = models.ForeignKey('Company', on_delete=models.RESTRICT)

    def __str__(self):
        return self.title


class Education(AbstractInfo):
    pass


class Experience(AbstractInfo):
    pass


class Certificate(AbstractInfo):
    link = models.URLField()


class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField()

    def __str__(self):
        return self.name
