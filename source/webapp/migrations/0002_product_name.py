# Generated by Django 2.2 on 2019-11-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
