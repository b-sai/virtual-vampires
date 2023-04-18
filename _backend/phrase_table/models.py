from django.db import models

# Create your models here.


class MyVerb(models.Model):
    english = models.CharField(max_length=50)
    spanish = models.CharField(max_length=50)

    def __str__(self):
        return self.english


class Pronoun(models.Model):
    english = models.CharField(max_length=50)
    spanish = models.CharField(max_length=50)

    def __str__(self):
        return self.english
