from django.db import models
from django_countries.fields import CountryField

from core.abstract_models import AbstractDefaultModel
from core.validators import check_phonenum, check_age


class Client(AbstractDefaultModel):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(max_length=255, verbose_name='Фамилия')
    age = models.IntegerField(
        verbose_name='возраст',
        validators= [check_age],
    )
    email = models.EmailField(verbose_name='почта')
    phone = models.CharField(
        max_length=13,
        validators=[check_phonenum],
        verbose_name='телефон'
    )
    location = CountryField(verbose_name='Страна')


    class Meta:
        ordering = ('first_name',)
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

class Balance(AbstractDefaultModel):
    value = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='количество денег')
    purchasers = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='покупатель'
    )

    class Meta:
        ordering = ('value',)
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'