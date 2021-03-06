from datetime import datetime,date

from tabnanny import verbose
from django.db import models

# Create your models here.

class Budjet(models.Model):
    Amoun_budjet = models.IntegerField("Сумма бюджета",default=0)
    Procent = models.IntegerField("процент прибыли",default=0)
    Bonus = models.IntegerField("Бонус",default=0)

    def __str__(self):
        return str(self.Amoun_budjet)

    class Meta:
        verbose_name = 'Бюджет'
        verbose_name_plural = 'Бюджеты'

class Jobposition(models.Model):
    Position = models.CharField('Должность',max_length=100)

    def __str__(self):
        return self.Position

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class Employees(models.Model):
    Full_name = models.CharField("ФИО",max_length=225)
    Position = models.ForeignKey(Jobposition,verbose_name = "Должность",null=True,on_delete=models.CASCADE)
    Salary = models.IntegerField("Оклад",default=0)
    Address = models.CharField("Адрес",max_length=150)
    Phone = models.IntegerField("Телефон",default=0)

    def __str__(self):
        return self.Full_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class  Units(models.Model):
    Unit = models.CharField("Единица измерения",max_length=100)

    def __str__(self):
        return self.Unit

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

class  Products(models.Model):
    Product = models.CharField("Продукт",max_length=150)
    Unit = models.ForeignKey(Units,verbose_name="Единица измерения",null=True,on_delete=models.SET_NULL)
    Summ = models.FloatField("Сумма",default=0)
    Amount = models.FloatField("Количество",default=0)    

    def __str__(self):
        return self.Product

    class Meta:
        verbose_name = 'Готовая продукция'
        verbose_name_plural = 'Готовые продукции'

class Rawmaterial(models.Model):
    Rm_name = models.CharField("Название",max_length=150)
    Unit = models.ForeignKey(Units,verbose_name="Единица измерения",null=True,on_delete=models.SET_NULL)
    Summ = models.FloatField("Сумма",default=0)
    Amount = models.FloatField("Количество",default=0)

    def __str__(self):
        return self.Rm_name

    class Meta:
        verbose_name = 'Сырьё'
        verbose_name_plural = 'Сырьё'

class Ingredients(models.Model):
    Product = models.ForeignKey(Products,verbose_name="Продукт",null=True,on_delete=models.CASCADE)
    Rm_name = models.ForeignKey(Rawmaterial,verbose_name="Сырьё",null=True,on_delete=models.SET_NULL)
    Amount = models.FloatField("Количество",default=0)

    def __str__(self):
        return str(self.Product)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

class Production(models.Model):
    Product = models.ForeignKey(Products,verbose_name="Продукт",null=True,on_delete=models.CASCADE)
    Amount = models.FloatField("Количество",default=0)
    Date = models.DateField("Дата производства")
    Employee = models.ForeignKey(Employees,verbose_name="Сотрудник",null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.Product)

    class Meta:
        verbose_name = 'Производство'
        verbose_name_plural = 'Производства'

class PurRawmaterial(models.Model):
    Rm_name = models.ForeignKey(Rawmaterial,verbose_name="Сырьё",null=True,on_delete=models.CASCADE)
    Amount = models.FloatField("Количество",default=0)
    Summ = models.FloatField("Сумма",default=0)
    Date = models.DateField("Дата покупки")
    Employee = models.ForeignKey(Employees,verbose_name="Сотрудник",null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.Rm_name),str(self.Date)

    class Meta:
        verbose_name = 'Покупка сырья'
        verbose_name_plural = 'Покупки сырья'

def default_datetime():
     return datetime.now()

def today_month():
    return date.today().strftime('%B')

def today_month():
    return date.today().strftime('%B')

class Month(models.Model):
    month = models.CharField("Месяц",max_length=255)

    def __str__(self):
        return self.month

    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцаы'

class SaleProduct(models.Model):
    Product = models.ForeignKey(Products,verbose_name="Продукт",null=True,on_delete=models.CASCADE)
    Amount = models.FloatField("Количество",default=0)
    Summ = models.FloatField("Сумма",default=0)
    Date = models.DateField("Дата продажи")
    Employee = models.ForeignKey(Employees,verbose_name="Сотрудник",null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.Product)

    class Meta:
        verbose_name = 'Продажа сырья'
        verbose_name_plural = 'Продажа сырья'


class Salaries(models.Model):
    Name = models.CharField("Имя сотрудника",max_length=255)
    Year = models.IntegerField("Год выдачи",default=0)
    Month = models.ForeignKey(Month, on_delete=models.SET_NULL,null=True,blank=True)
    Purchases = models.IntegerField("Покупка",default=0)
    Sales = models.IntegerField("Продажа",default=0)
    Production = models.IntegerField("Производство",default=0)
    TotalPart = models.IntegerField("Участие",default=0)
    Bonus = models.IntegerField("Бонус",default=0)
    Salary = models.IntegerField("Оклад",default=0)
    IsGiven = models.BooleanField("Выдано",default=False)
    TotalSum = models.IntegerField("Общая сумма",default=0)

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name = 'Выдача ЗП'
        verbose_name_plural = 'Выдача ЗП'
