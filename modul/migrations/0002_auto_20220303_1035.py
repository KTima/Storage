# Generated by Django 3.2.7 on 2022-03-03 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modul', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='Rm_name',
        ),
        migrations.AddField(
            model_name='ingredients',
            name='Rm_name',
            field=models.ManyToManyField(null=True, to='modul.Rawmaterial', verbose_name='Сырьё'),
        ),
    ]