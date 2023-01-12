from django.db import models
from django_countries.fields import CountryField

from core.abstract_models import AbstractDefaultModel


class Supplier(AbstractDefaultModel):
    name = models.CharField(max_length=255, verbose_name='Имя')
    location = CountryField(verbose_name='Страна')
    email = models.EmailField(verbose_name='почта')
    product = models.CharField(max_length=255, verbose_name='Товар')
    reviews = models.TextField(max_length=500, verbose_name='Отзывы')


    class Meta:
        ordering = ('name',)
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name