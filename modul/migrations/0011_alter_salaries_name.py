# Generated by Django 3.2.7 on 2022-04-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modul', '0010_auto_20220405_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaries',
            name='Name',
            field=models.CharField(max_length=255, verbose_name='Имя сотрудника'),
        ),
    ]
