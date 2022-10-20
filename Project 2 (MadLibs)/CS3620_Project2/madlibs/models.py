from django.db import models


# Create your models here.
class Madlibs(models.Model):

    def __str__(self):
        return self.noun + self.adjective + self.city + self.noun2 + self.pronoun + self.verb + self.noun3

    noun = models.CharField(max_length=20, default="")
    adjective = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=20, default="")
    noun2 = models.CharField(max_length=20, default="")
    pronoun = models.CharField(max_length=20, default="")
    verb = models.CharField(max_length=20, default="")
    noun3 = models.CharField(max_length=20, default="")
