from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',  verbose_name='Пользователь')

    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')


    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Профиль'

        verbose_name_plural = 'Профили'