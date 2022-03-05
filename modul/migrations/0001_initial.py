# Generated by Django 3.2.7 on 2022-02-23 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amoun_budjet', models.IntegerField(default=0, verbose_name='Сумма бюджета')),
            ],
            options={
                'verbose_name': 'Бюджет',
                'verbose_name_plural': 'Бюджеты',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=225, verbose_name='ФИО')),
                ('Salary', models.IntegerField(default=0, verbose_name='Оклад')),
                ('Address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('Phone', models.IntegerField(default=0, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Jobposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(max_length=100, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.CharField(max_length=150, verbose_name='Продукт')),
                ('Summ', models.IntegerField(default=0, verbose_name='Сумма')),
                ('Amount', models.IntegerField(default=0, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Готовая продукция',
                'verbose_name_plural': 'Готовые продукции',
            },
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit', models.CharField(max_length=100, verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единицы измерения',
            },
        ),
        migrations.CreateModel(
            name='SaleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField(default=0, verbose_name='Количество')),
                ('Summ', models.IntegerField(default=0, verbose_name='Сумма')),
                ('Date', models.DateField(verbose_name='Дата продажи')),
                ('Employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modul.employees', verbose_name='Сотрудник')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modul.products', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Продажа сырья',
                'verbose_name_plural': 'Продажа сырья',
            },
        ),
        migrations.CreateModel(
            name='Rawmaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rm_name', models.CharField(max_length=150, verbose_name='Название')),
                ('Summ', models.IntegerField(default=0, verbose_name='Сумма')),
                ('Amount', models.IntegerField(default=0, verbose_name='Количество')),
                ('Unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modul.units', verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Сырьё',
                'verbose_name_plural': 'Сырьё',
            },
        ),
        migrations.CreateModel(
            name='PurRawmaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField(default=0, verbose_name='Количество')),
                ('Summ', models.IntegerField(default=0, verbose_name='Сумма')),
                ('Date', models.DateField(verbose_name='Дата покупки')),
                ('Employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modul.employees', verbose_name='Сотрудник')),
                ('Rm_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modul.rawmaterial', verbose_name='Сырьё')),
            ],
            options={
                'verbose_name': 'Покупка сырья',
                'verbose_name_plural': 'Покупки сырья',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='Unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modul.units', verbose_name='Единица измерения'),
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField(default=0, verbose_name='Количество')),
                ('Date', models.DateField(verbose_name='Дата производства')),
                ('Employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modul.employees', verbose_name='Сотрудник')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modul.products', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Производство',
                'verbose_name_plural': 'Производства',
            },
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField(default=0, verbose_name='Количество')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modul.products', verbose_name='Продукт')),
                ('Rm_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modul.rawmaterial', verbose_name='Сырьё')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.AddField(
            model_name='employees',
            name='Position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modul.jobposition', verbose_name='Должность'),
        ),
    ]
