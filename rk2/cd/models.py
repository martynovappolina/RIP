from django.db import models


class CD_lib(models.Model):
    """библиотека cd-дисков"""
    objects = models.Manager()
    name = models.CharField(max_length=50, verbose_name="Название библиотеки")


class CD(models.Model):
    """cd-диск"""
    objects = models.Manager()
    name = models.CharField(max_length=50, verbose_name="Название диска")
    capacity = models.CharField(max_length=50, verbose_name="Ёмкость диска")
    cdLib = models.ForeignKey(CD_lib, on_delete=models.CASCADE, null=True)
