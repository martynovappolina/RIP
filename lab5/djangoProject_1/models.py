from django.db import models


# Create your models here.
class Theatre(models.Model):
    name = models.CharField(max_length=30)
    discription = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'theatre'
