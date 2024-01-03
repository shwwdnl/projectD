
from django.db import models

from config import settings

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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='продавец', **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.price})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_num = models.CharField(max_length=30, verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    version_indication = models.BooleanField(default=False, verbose_name='Текущая версия')

    def __str__(self):
        return f'{self.product} ({self.version_num})'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


