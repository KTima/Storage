from . import views
from django.urls import path

urlpatterns = [
    path("",views.Views,name = 'Home'),
    path("budjet",views.BudgetView.as_view(), name = 'budget'),
    path('budjet/<int:pk>',views.BudjetUpdateView.as_view(),name = 'budjetsupdate'),
    path('budjetdelete/<int:pk>',views.BudjetDeleteView.as_view(),name = 'budjetsdelete'),

    path("positions",views.PositionstView.as_view(), name = 'positions'),
    path('position/<int:pk>',views.PositionUpdateView.as_view(),name = 'positionupdate'),
    path('positiondelete/<int:pk>',views.PositionDeleteView.as_view(),name = 'positiondelete'),

    path("employee",views.EmployeeView.as_view(), name = 'employee'),
    path('employee/<int:pk>',views.EmployeeUpdateView.as_view(),name = 'employeeupdate'),
    path('employeedelete/<int:pk>',views.EmployeeDeleteView.as_view(),name = 'employeedelete'),

    path("unit",views.UnitsView.as_view(), name = 'unit'),
    path('unit/<int:pk>',views.UnitUpdateView.as_view(),name = 'unitupdate'),
    path('unitdelete/<int:pk>',views.UnitDeleteView.as_view(),name = 'unitdelete'),

    path("product",views.ProductsView.as_view(), name = 'product'),
    path('product/<int:pk>',views.ProductUpdateView.as_view(),name = 'productupdate'),
    path('productdelete/<int:pk>',views.ProductDeleteView.as_view(),name = 'productdelete'),

    path("rawmaterial",views.RawsView.as_view(), name = 'raw'),
    path('rawmaterial/<int:pk>',views.RawUpdateView.as_view(),name = 'rawupdate'),
    path('rawdelete/<int:pk>',views.RawDeleteView.as_view(),name = 'rawdelete'),

    path("purchase",views.PurView.as_view(), name = 'pur'),
    path('purchaseup/<int:id>',views.PurchaseUpdateView.as_view(),name = 'purupdate'),
    path('purchasedel/<int:pk>',views.PurchaseDeleteView.as_view(),name = 'purdelete'),

    path("ingredient",views.IngrView.as_view(), name = 'ing'),
    path('ingredient/<int:pk>',views.IngUpdateView.as_view(),name = 'ingupdate'),
    path('ingdelete/<int:pk>',views.IngDeleteView.as_view(),name = 'ingdelete'),

    path("sale",views.SaleView.as_view(), name = 'sale'),
    path('saleupdate/<int:pk>',views.SaleUpdateView.as_view(),name = 'saleupdate'),
    path('saledelete/<int:pk>',views.SaleDeleteView.as_view(),name = 'saledelete'),

    path("production",views.ProdutionView.as_view(), name = 'production'),
    path('productionupdate/<int:pk>',views.ProductionUpdateView.as_view(),name = 'productionupdate'),
    path('productiondelete/<int:pk>',views.ProductionDeleteView.as_view(),name = 'productiondelete'),

    path('createbudjet',views.CreateBudjet,name = 'createbudjet'),
    path('createposition',views.CreatePosition,name = 'createposition'),
    path('createemployee',views.CreateEmployee,name = 'createemployee'),
    path('createunit',views.CreateUnit,name = 'createunit'),
    path('createproduct',views.CreateProduct,name = 'createproduct'),
    path('createrawmaterial',views.CreateRaw,name = 'createraw'),
    path('createingredient',views.CreateIng,name = 'createingredient'),
    path('createpurchase',views.CreatePurchase,name = 'createpurchase'),
    path('createsale',views.CreateSale,name = 'createsale'),
    path('createproduction',views.CreateProduction,name = 'createproduction'),
    path('createsalaries',views.CreateSalaries,name = 'createsalaries'),
    path('searchsalaries',views.SearchSalaries,name = 'searchsalaries'),

]