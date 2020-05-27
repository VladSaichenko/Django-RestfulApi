from django.db import models


class Paradigm(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=24)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=25)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
