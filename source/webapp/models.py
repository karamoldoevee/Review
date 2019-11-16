from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    SMARTPHONE = 'SM'
    LAPTOP = 'LP'
    EARPHONE = 'ER'
    CATEGORY_CHOICES = [
        ('SM', 'Smartphone'),
        ('LP', 'Laptop'),
        ('ER', 'Earphone'),
    ]
    name = models.CharField(max_length=100, blank=False, verbose_name='Название')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=SMARTPHONE, verbose_name='Категория')
    description = models.TextField(max_length=2000, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Картинка')

class Review(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, default=None, verbose_name='Автор', on_delete=models.CASCADE,
                               related_name='review')
    product = models.ForeignKey('webapp.Product', related_name='review', on_delete=models.CASCADE, verbose_name='Продукт')

    text = models.TextField(max_length=400, verbose_name='Текст отзыва')
    raiting = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=False, blank=False)


