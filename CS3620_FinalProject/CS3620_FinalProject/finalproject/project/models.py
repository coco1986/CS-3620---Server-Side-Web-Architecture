from django.db import models


# Create your models here.

# this class is based on the user's information
class Build(models.Model):
    def __str__(self):
        return self.battle_name

    battle_name = models.CharField(max_length=100)
    monster_build = models.CharField(max_length=100)
    skill_1 = models.TextField(max_length=1000)
    equip_1 = models.CharField(max_length=200)
    skill_2 = models.TextField(max_length=1000)
    equip_2 = models.CharField(max_length=200)
    skill_3 = models.TextField(max_length=1000)
    equip_3 = models.CharField(max_length=200)
    strategy = models.TextField(max_length=5000)
