
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import *
from django.forms import ModelForm,DateInput

class BudjetForm(ModelForm):
    class Meta:
        model = Budjet
        fields = ['Amoun_budjet','Procent']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))
        
class PositionForm(ModelForm):
    class Meta:
        model = Jobposition
        fields = ['Position']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

class EmployeeForm(ModelForm):
    class Meta:
        model = Employees
        fields = ['Full_name','Position','Salary','Address','Phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))


class UnitForm(ModelForm):
    class Meta:
        model = Units
        fields = ['Unit']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['Product','Unit','Summ','Amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))


class RawForm(ModelForm):
    class Meta:
        model = Rawmaterial
        fields = ['Rm_name','Unit','Summ','Amount']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

class IngForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = ['Product','Rm_name','Amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

class PurchaseForm(ModelForm):
    class Meta:
        model = PurRawmaterial
        fields = ['Rm_name','Amount','Summ','Date','Employee']

        widgets = {
            "Date":DateInput(attrs={'type': 'date'} ),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

class SaleForm(ModelForm):
    class Meta:
        model = SaleProduct
        fields = ['Product','Amount','Date','Employee']

        widgets = {
            "Date":DateInput(attrs={'type': 'date'} ),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

class ProductionForm(ModelForm):
    class Meta:
        model = Production
        fields = ['Product','Amount','Date','Employee']

        widgets = {
            "Date":DateInput(attrs={'type': 'date'} ),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))