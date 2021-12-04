from django.db import models

# Create your models here.

from django.db import models


class Stock(models.Model):
    company_name = models.CharField(max_length=50, verbose_name="Название спектакля")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Рейтинг")
    is_growing = models.BooleanField(verbose_name="Набирается ли полный зал?")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Дата")