from django.contrib import admin
from .models import PizzaTopping, RegularPizza, SicilianPizza, Sub, Pasta, Salad, DinnerPlatter, Orders, ActiveOrders

# Register your models here.
admin.site.register(PizzaTopping)
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(Orders)
admin.site.register(ActiveOrders)