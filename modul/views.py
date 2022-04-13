from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from modul.models import *
from .forms import *
from django.views.generic import UpdateView,DeleteView,ListView
from django.db.models import Q
from .filters import *
from django.db.models import Sum

# Create your views here.

def Views(request):
    return render(request, 'modul/home.html')

def CreateBudjet(request):
    error = ''
    if request.method == 'POST':
        form = BudjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget')
        else:
            error = "Форма была неверно введена"
    form = BudjetForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'modul/createbudjet.html',context)

def CreatePosition(request):
    error = ''
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('positions')
        else:
            error = "Форма была неверно введена"
    form = PositionForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'modul/createposition.html',context)

def CreateEmployee(request):
    error = ''
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee')
        else:
            error = "Форма была неверно введена"
    form = EmployeeForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'modul/createemployee.html',context)

def CreateUnit(request):
    error = ''
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit')
        else:
            error = "Форма была неверно введена"
    form = UnitForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'modul/createunit.html',context)

def CreateProduct(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
        else:
            error = "Форма была неверно введена"
    form = ProductForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'modul/createproduct.html',context)

def CreateRaw(request):
    error = ''
    if request.method == 'POST':
        form = RawForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('raw')
        else:
            error = "Форма была неверно введена"
    form = RawForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'modul/createraw.html',context)

def CreateIng(request):
    error = ''
    if request.method == 'POST':
        form = IngForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ing')
        else:
            error = "Форма была неверно введена"
    form = IngForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'modul/createing.html',context)

def CreatePurchase(request):
    error = ''
    budjet = Budjet.objects.get(id=24)
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        summ = request.POST.get('Summ')
        rm_name = request.POST.get('Rm_name')
        amount = request.POST.get('Amount')
        raw = Rawmaterial.objects.get(id=rm_name)
        if form.is_valid():
            if float(summ)<= budjet.Amoun_budjet:
                budjet.Amoun_budjet = budjet.Amoun_budjet-float(summ)
                raw.Summ = raw.Summ + float(summ)
                raw.Amount = raw.Amount + float(amount)
                raw.save()
                budjet.save()
                form.save()
                return redirect('pur')
            else:
                error = (f"Увас не хватает {float(summ) - budjet.Amoun_budjet} в бюджете")
        else:
            error = "Форма была неверно введена"
    form = PurchaseForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'modul/createpurchase.html',context)

def CreateSale(request):
    error = ''
    budjet = Budjet.objects.get(id=24)
    if request.method == 'POST':
        form = SaleForm(request.POST)
        pr = request.POST.get('Product')
        amount = request.POST.get('Amount')
        date = request.POST.get('Date')
        products = Products.objects.get(id=pr)
        seb = 0
        if form.is_valid():
            if float(amount)<=products.Amount:
                seb = products.Summ / products.Amount
                summ = (float(seb) * float(amount)) + ((float(seb) * float(amount) / 100 ) * budjet.Procent)
                products.Summ = products.Summ - float(seb)*float(amount)
                products.Amount = products.Amount - float(amount)
                budjet.Amoun_budjet = budjet.Amoun_budjet + summ
                budjet.Date = date
                budjet.save()
                products.save()
                response = form.save()
                response.Summ = summ
                response.save()
                return redirect('sale')
            else:
                error = "Недостаточно количества продукта"
        else:
            error = "Форма была неверно введена"
    form = SaleForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'modul/createsale.html',context)

def CreateProduction(request):
    error = ''
    spisok = []
    if request.method == 'POST':
        form = ProductionForm(request.POST)
        pr = request.POST.get('Product')
        amount = request.POST.get('Amount')
        ingrs = Ingredients.objects.all().filter(Product_id = pr)
        rm = Rawmaterial.objects.all()
        prod = Products.objects.get(id=pr)
        if form.is_valid():
            for i in ingrs:
                rm = Rawmaterial.objects.get(Rm_name=i.Rm_name.Rm_name)
                if i.Amount <= rm.Amount:
                    if (rm.Amount - float(amount) * i.Amount) >= 0:
                        spisok.append(True)
                    else:
                        spisok.append(False)
                        error = "Не хватает"
                else:
                    error = "Не хватает"
            if spisok.count(False) == 0:
                summ = 0
                for ingr in ingrs:
                    rm = Rawmaterial.objects.get(Rm_name=ingr.Rm_name.Rm_name)
                    seb_rm = rm.Summ / rm.Amount
                    summ += (rm.Summ /rm.Amount * ingr.Amount * float(amount))
                    rm.Amount = rm.Amount - float(amount) * ingr.Amount
                    rm.Summ = rm.Summ - (seb_rm * (float(amount) * ingr.Amount))
                    rm.save()
                prod.Amount = prod.Amount + float(amount) 
                prod.Summ = prod.Summ + summ
                prod.save()
                form.save()
                return redirect('production')
            else:
                error = "Не хватает"
        else:
            error = "Форма была неверно введена"
    form = ProductionForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'modul/createproduction.html',context)

class BudgetView(ListView):
    model = Budjet 
    template_name = 'modul/budjet.html'
    context_object_name = 'budjets'

class PositionstView(ListView):
    model = Jobposition 
    template_name = 'modul/position.html'
    context_object_name = 'positions'

class EmployeeView(ListView):
    model = Employees
    template_name = 'modul/employee.html'
    context_object_name = 'employees'

class UnitsView(ListView):
    model = Units
    template_name = 'modul/unit.html'
    context_object_name = 'units'

class ProductsView(ListView):
    model = Products
    template_name = 'modul/product.html'
    context_object_name = 'products'

class RawsView(ListView):
    model = Rawmaterial
    template_name = 'modul/raw.html'
    context_object_name = 'raws'

class PurView(ListView):
    model = PurRawmaterial
    template_name = 'modul/pur.html'
    context_object_name = 'purchases'

class SaleView(ListView):
    model = SaleProduct
    template_name = 'modul/sale.html'
    context_object_name = 'sales'

class ProdutionView(ListView):
    model = Production
    template_name = 'modul/production.html'
    context_object_name = 'productions'

class IngrView(ListView):
    model = Ingredients
    template_name = 'modul/ing.html'

    def get_queryset(self):
        query = self.request.GET.get('ingrs')
        if query == "allser":
            object_list = Ingredients.objects.all()
            return object_list
        if query == "Мотор":
            object_list = Ingredients.objects.filter(
                    Q(Product__id__icontains=2)
                    )
            return object_list
        if query == "Машина":
            object_list = Ingredients.objects.filter(
                    Q(Product__id__icontains=6)
                    )
            return object_list
        if query == "Шины":
            object_list = Ingredients.objects.filter(
                    Q(Product__id__icontains=3)
                    )
            return object_list

class BudjetUpdateView(UpdateView):
    model = Budjet
    template_name = 'modul/createbudjet.html'
    form_class = BudjetForm
    success_url = reverse_lazy("budget")

class BudjetDeleteView(DeleteView):
    model = Budjet
    template_name = 'modul/budjet.html'
    success_url = reverse_lazy("budget")

class PositionUpdateView(UpdateView):
    model = Jobposition
    template_name = 'modul/createposition.html'
    form_class = PositionForm
    success_url = reverse_lazy('positions')

class PositionDeleteView(DeleteView):
    model = Jobposition
    template_name = 'modul/position.html'
    success_url = reverse_lazy("positions")

class EmployeeUpdateView(UpdateView):
    model = Employees
    template_name = 'modul/createemployee.html'
    form_class = EmployeeForm
    success_url = reverse_lazy("employee")

class EmployeeDeleteView(DeleteView):
    model = Employees
    template_name = 'modul/employee.html'
    success_url = reverse_lazy("employee")

class UnitUpdateView(UpdateView):
    model = Units
    template_name = 'modul/createunit.html'
    form_class = UnitForm
    success_url = reverse_lazy("unit")

class UnitDeleteView(DeleteView):
    model = Units
    template_name = 'modul/unit.html'
    success_url = reverse_lazy("unit")

class ProductUpdateView(UpdateView):
    model = Products
    template_name = 'modul/createproduct.html'
    form_class = ProductForm
    success_url = reverse_lazy("product")

class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'modul/product.html'
    success_url = reverse_lazy("product")

class RawUpdateView(UpdateView):
    model = Rawmaterial
    template_name = 'modul/createraw.html'
    form_class = RawForm
    success_url = reverse_lazy("raw")

class RawDeleteView(DeleteView):
    model = Rawmaterial
    template_name = 'modul/raw.html'
    success_url = reverse_lazy("raw")

class IngUpdateView(UpdateView):
    model = Ingredients
    template_name = 'modul/createing.html'
    form_class = IngForm
    success_url = reverse_lazy("ing")

class IngDeleteView(DeleteView):
    model = Ingredients
    template_name = 'modul/ing.html'
    success_url = reverse_lazy("ing")

class PurchaseUpdateView(UpdateView):
    model = PurRawmaterial
    template_name = 'modul/createpurchase.html'
    form_class = PurchaseForm
    success_url = reverse_lazy("pur")

class PurchaseDeleteView(DeleteView):
    model = PurRawmaterial
    template_name = 'modul/pur.html'
    success_url = reverse_lazy("pur")

class SaleUpdateView(UpdateView):
    model = SaleProduct
    template_name = 'modul/createsale.html'
    form_class = SaleForm
    success_url = reverse_lazy("sale")

class SaleDeleteView(DeleteView):
    model = SaleProduct
    template_name = 'modul/sale.html'
    success_url = reverse_lazy("sale")

class ProductionUpdateView(UpdateView):
    model = Production
    template_name = 'modul/createproduction.html'
    form_class = ProductionForm
    success_url = reverse_lazy("production")

class ProductionDeleteView(DeleteView):
    model = Production
    template_name = 'modul/production.html'
    success_url = reverse_lazy("production")

def CreateSalaries(request):
    error = ''
    if request.method == 'POST':
        budjet = Budjet.objects.get(id=24)
        sotr = Employees.objects.all()
        year = request.POST.get('Year')
        month = request.POST.get('Month')
        pur = PurRawmaterial.objects.all().filter(Date__year = year, Date__month = int(month))
        sal = SaleProduct.objects.all().filter(Date__year = year, Date__month = int(month))
        pro = Production.objects.all().filter(Date__year = year, Date__month = int(month))
        form = SalariesForm(request.POST)
        if form.is_valid():
            prsl = Salaries.objects.all().filter(Year = year,Month_id=month)
            if len(prsl) == 0:
                for i in sotr:
                    purcount = 0
                    salcount = 0
                    procount = 0
                    bon = i.Salary / 100 * budjet.Bonus
                    for j in pur:
                        if j.Employee.Full_name == i.Full_name:
                            purcount += 1          
                    for k in sal:
                        if k.Employee.Full_name == i.Full_name:
                            salcount += 1
                    for d in pro:
                        if d.Employee.Full_name == i.Full_name:
                            procount += 1
                    Salaries.objects.create(Name=i.Full_name,
                    Year=year,
                    Month_id=month,
                    Purchases = purcount,
                    Sales = salcount,
                    Production = procount,
                    TotalPart = purcount + salcount + procount,
                    Bonus = budjet.Bonus,
                    Salary = i.Salary,
                    TotalSum = i.Salary + (bon * (purcount + salcount + procount)),
                    )
                return redirect('searchsalaries')
            else:
                error = 'Такой данные уже существуют'
        else:
            error = "Форма была неверно введена"
    form = SalariesForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'modul/createsalaries.html',context)

def SearchSalaries(request):
    error = ''
    sr = Salaries.objects.all().order_by('-pk')
    budjet = Budjet.objects.get(id=24)
    summ=0
    if request.method == 'GET':
        MyFilter = SalariesFilter(request.GET,queryset=sr)
        sr = MyFilter.qs
        for k in MyFilter.qs:
            summ=k.TotalSum+summ
        if 'Oplatit' in request.GET:
            for i in MyFilter.qs:
                sd=i.Year
                pd=i.Month
            op = Salaries.objects.all().filter(Year = sd)
            for a in op:
                if a.IsGiven == False: 
                    if budjet.Amoun_budjet - summ > 0:
                        op = Salaries.objects.all().filter(Year = sd,Month=pd)
                        budjet.Amoun_budjet = budjet.Amoun_budjet - summ
                        budjet.save()
                        for a in op:
                            a.IsGiven = True
                            a.save()
                        sr.update()
                        return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
                    
                    else:
                        error = "Не хватает суммы в буджете"
                else:
                    error = "Уже оплачено"
    context = {
    'summ':summ,
    'error':error,
    'sr':sr,
    'MyFilter':MyFilter,
    }
    return render(request,'modul/salaries.html',context)