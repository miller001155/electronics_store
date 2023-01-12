from django.db import models

from core.abstract_models import AbstractDefaultModel


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(AbstractDefaultModel):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Инвентаризация')
    available = models.BooleanField(default=True, verbose_name='Доступность на складе')

    class Meta:
        ordering = ('name',)
        index_together = (('category', 'slug'),)

    def __str__(self):
        return self.name
