from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from modul.models import *
from .forms import *
from django.views.generic import UpdateView,DeleteView
from django.db.models import Q

# Create your views here.

def Views(request):
    return render(request, 'modul/index.html')

def CreateBudjet(request):
    error = ''
    if request.method == 'POST':
        form = BudjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
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
            return redirect('Home')
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
            return redirect('Home')
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
            return redirect('Home')
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
            return redirect('Home')
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
            return redirect('Home')
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
            return redirect('Home')
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
            if int(summ)<= budjet.Amoun_budjet:
                budjet.Amoun_budjet = budjet.Amoun_budjet-int(summ)
                raw.Summ = raw.Summ + int(summ)
                raw.Amount = raw.Amount + int(amount)
                raw.save()
                budjet.save()
                form.save()
                return redirect('Home')
            else:
                error = (f"Увас не хватает {int(summ) - budjet.Amoun_budjet} в бюджете")
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
            if int(amount)<=products.Amount:
                seb = products.Summ / products.Amount
                summ = (int(seb) * int(amount)) + ((int(seb) * int(amount) / 100 ) * budjet.Procent)
                products.Summ = products.Summ - int(seb)*int(amount)
                products.Amount = products.Amount - int(amount)
                budjet.Amoun_budjet = budjet.Amoun_budjet + summ
                budjet.Date = date
                budjet.save()
                products.save()
                response = form.save()
                response.Summ = summ
                response.save()
                return redirect('Home')
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
                    if (rm.Amount - int(amount) * i.Amount) >= 0:
                        spisok.append(True)
                    else:
                        spisok.append(False)
                        error = "Не хватает"
                else:
                    error = "Не хватает"
            if spisok.count(False) == 0:
                for ingr in ingrs:
                    rm = Rawmaterial.objects.get(Rm_name=ingr.Rm_name.Rm_name)
                    seb_rm = rm.Summ / rm.Amount
                    rm.Amount = rm.Amount - int(amount) * ingr.Amount
                    rm.Summ = rm.Summ - (seb_rm * (int(amount) * ingr.Amount))
                    rm.save()
                seb_prod = prod.Summ / prod.Amount
                prod.Amount = prod.Amount + int(amount) 
                prod.Summ = prod.Summ + (int(seb_prod) * int(amount))
                prod.save()
                form.save()
                return redirect('Home')
            else:
                error = "Не хватает"
        else:
            error = "Форма была неверно введена"
    form = ProductionForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'modul/createproduction.html',context)

def IndexView(request):
    budjets = Budjet.objects.all()
    positions = Jobposition.objects.all()
    employees = Employees.objects.all()
    units = Units.objects.all()
    products = Products.objects.all()
    raws = Rawmaterial.objects.all()
    purchases = PurRawmaterial.objects.all()
    sales = SaleProduct.objects.all()
    productions = Production.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        ings = Ingredients.objects.filter(Q(Product__Product__icontains = search))
        context = {
            "budjets":budjets,
            "positions":positions,
            "employees":employees,
            "units":units,
            "products":products,
            "raws":raws,
            "purchases":purchases,
            "sales":sales,
            "productions":productions,
            "ings":ings
        }
        return render(request,"modul/index.html",context)
    else:
        context1 = {
            "budjets":budjets,
            "positions":positions,
            "employees":employees,
            "units":units,
            "products":products,
            "raws":raws,
            "purchases":purchases,
            "sales":sales,
            "productions":productions,
        }
        return render(request,"modul/index.html",context1)

class BudjetUpdateView(UpdateView):
    model = Budjet
    template_name = 'modul/createbudjet.html'
    form_class = BudjetForm
    success_url = reverse_lazy("Home")

class BudjetDeleteView(DeleteView):
    model = Budjet
    template_name = 'modul/index.html'
    success_url = reverse_lazy("Home")

class PositionUpdateView(UpdateView):
    model = Jobposition
    template_name = 'modul/createposition.html'
    form_class = PositionForm
    success_url = reverse_lazy('Home')

class PositionDeleteView(DeleteView):
    model = Jobposition
    template_name = 'modul/index.html'
    success_url = reverse_lazy("Home")


class EmployeeUpdateView(UpdateView):
    model = Employees
    template_name = 'modul/createemployee.html'
    form_class = EmployeeForm
    success_url = reverse_lazy("Home")

class EmployeeDeleteView(DeleteView):
    model = Employees
    template_name = 'modul/index.html'
    success_url = reverse_lazy("Home")


class UnitUpdateView(UpdateView):
    model = Units
    template_name = 'modul/createunit.html'
    form_class = UnitForm
    success_url = reverse_lazy("Home")

class UnitDeleteView(DeleteView):
    model = Units
    template_name = 'modul/index.html'
    success_url = reverse_lazy("Home")


class ProductUpdateView(UpdateView):
    model = Products
    template_name = 'modul/createproduct.html'
    form_class = ProductForm
    success_url = reverse_lazy("Home")

class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'modul/index.html'
    success_url = reverse_lazy("Home")

class RawUpdateView(UpdateView):
    model = Rawmaterial
    template_name = 'modul/createraw.html'
    form_class = RawForm
    success_url = reverse_lazy("Home")

class RawDeleteView(DeleteView):
    model = Rawmaterial
    template_name = 'modul/index.html'
    success_url = reverse_lazy("Home")

class IngUpdateView(UpdateView):
    model = Ingredients
    template_name = 'modul/createing.html'
    form_class = IngForm
    success_url = reverse_lazy("Home")

class IngDeleteView(DeleteView):
    model = Ingredients
    template_name = 'modul/index.html'
    success_url = reverse_lazy("Home")

class PurchaseUpdateView(UpdateView):
    model = PurRawmaterial
    template_name = 'modul/createpurchase.html'
    form_class = PurchaseForm
    success_url = reverse_lazy("Home")

class PurchaseDeleteView(DeleteView):
    model = PurRawmaterial
    template_name = 'modul/index.html'
    success_url = reverse_lazy("Home")

class SaleUpdateView(UpdateView):
    model = SaleProduct
    template_name = 'modul/createsale.html'
    form_class = SaleForm
    success_url = reverse_lazy("Home")

class SaleDeleteView(DeleteView):
    model = SaleProduct
    template_name = 'modul/index.html'
    success_url = reverse_lazy("Home")

class ProductionUpdateView(UpdateView):
    model = Production
    template_name = 'modul/createproduction.html'
    form_class = ProductionForm
    success_url = reverse_lazy("Home")

class ProductionDeleteView(DeleteView):
    model = Production
    template_name = 'modul/index.html'
    success_url = reverse_lazy("Home")