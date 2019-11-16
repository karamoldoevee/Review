# from django.conf import settings
# from django.db import models
#
#
#
# class Product(models.Model):
#     SMARTPHONE = 'SM'
#     LAPTOP = 'LP'
#     EARPHONE = 'ER'
#     CATEGORY_CHOICES = [
#         ('SM', 'Smartphone'),
#         ('LP', 'Laptop'),
#         ('ER', 'Earphone'),
#     ]
#     name = models.CharField(max_length=100, blank=False, verbose_name='Название'),
#     category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=SMARTPHONE, verbose_name='Категория')
#     description = models.TextField(max_length=2000, blank=True, verbose_name='Описание')
#     image = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Картинка')
#
# class Review(models.Model):
#     author


