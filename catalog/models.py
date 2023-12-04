
from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class Category(models.Model):
    name = models.CharField(**NULLABLE, max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Стоимость')
    created_at = models.DateTimeField(**NULLABLE, auto_now_add=True, verbose_name='Дата создания')
    mod_at = models.DateTimeField(**NULLABLE, auto_now=True, verbose_name='Дата изменения')
    owner = models.CharField(max_length=100, verbose_name='продавец', **NULLABLE)
    def __str__(self):
        return f'{self.name} ({self.price})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
