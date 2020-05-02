from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PizzaTopping(models.Model):
    topping = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "3. Pizza Toppings"
    
    def __str__(self):
        return f"Pizza Topping {self.topping}"

class RegularPizza(models.Model):
    pizza_type = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    num_toppings = models.PositiveSmallIntegerField()
    cost = models.FloatField()
    
    class Meta:
        verbose_name_plural = "4. Regular Pizza"

    def __str__(self):
        return f"Regular Pizza {self.pizza_type} - Size: {self.size} - {self.num_toppings} Toppings - Cost: ${self.cost}"

class SicilianPizza(models.Model):
    pizza_type = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    num_toppings = models.PositiveSmallIntegerField()
    cost = models.FloatField()

    class Meta:
        verbose_name_plural = "5. Sicilian Pizza"
    
    def __str__(self):
        return f"Sicilian Pizza {self.pizza_type} - Size: {self.size} - {self.num_toppings} Toppings - Cost: ${self.cost}"

class Sub(models.Model):
    sub_type = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    cost = models.FloatField()

    class Meta:
        verbose_name_plural = "6. Subs"

    def __str__(self):
        return f"Sub {self.sub_type} - Size: {self.size} - Cost: ${self.cost}"

class Pasta(models.Model):
    pasta_type = models.CharField(max_length=64)
    cost = models.FloatField()

    class Meta:
        verbose_name_plural = "7. Pasta"

    def __str__(self):
        return f"Pasta {self.pasta_type} - Cost: ${self.cost}"

class Salad(models.Model):
    salad_type = models.CharField(max_length=64)
    cost = models.FloatField()

    class Meta:
        verbose_name_plural = "8. Salad"

    def __str__(self):
        return f"Salad {self.salad_type} - Cost: ${self.cost}"

class DinnerPlatter(models.Model):
    dinner_platter_type = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    cost = models.FloatField()

    class Meta:
        verbose_name_plural = "9. Dinner Platter"

    def __str__(self):
        return f"Dinner Platter {self.dinner_platter_type} - Size: {self.size} - Cost: ${self.cost}"

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=64)
    item_type = models.CharField(max_length=64)
    size = models.CharField(max_length=64, blank=True)
    cost = models.FloatField()
    # Specifics for Topping Pizza
    num_toppings = models.PositiveSmallIntegerField(blank=True, null=True)
    pizza_toppings = models.ManyToManyField(PizzaTopping, blank=True, related_name="toppings")
    
    order_placed = models.BooleanField(default=False)
    order_completed = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "2. Cart Items"

    def __str__(self):
        return f"{self.user} - {self.product_type} {self.item_type} - Cost: ${self.cost} - Order Placed: {self.order_placed}"

class ActiveOrders(models.Model):
    order = models.ForeignKey(Orders, null=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name_plural = "1. Active Orders for Fulfillment"

    def __str__(self):
        return f"{self.order} - Start: {self.start_date}"