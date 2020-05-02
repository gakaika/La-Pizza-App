from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import RegularPizza, SicilianPizza, Sub, Pasta, Salad, DinnerPlatter, PizzaTopping, Orders, ActiveOrders

def index(request):
    context = {
        "reg_pizza_types": RegularPizza.objects.values_list('pizza_type', flat=True).distinct(),
        "sicilian_pizza_types": SicilianPizza.objects.values_list('pizza_type', flat=True).distinct(),
        "sub_types": Sub.objects.values_list('sub_type', flat=True).distinct(),
        "pasta_types": Pasta.objects.values_list('pasta_type', flat=True).distinct(),
        "salad_types": Salad.objects.values_list('salad_type', flat=True).distinct(),
        "dinner_platter_types": DinnerPlatter.objects.values_list('dinner_platter_type', flat=True).distinct()
    }

    return render(request, "orders/index.html", context)

def product_view(request, product_type, item_type):
    if product_type=="Regular Pizza":
        if item_type not in RegularPizza.objects.values_list('pizza_type', flat=True).distinct():
            return render(request, "orders/error.html", {"error": "Invalid Product"})
        context = {
            "product_type": product_type,
            "item_type": item_type,
            "product": item_type + " Pizza",
            "image_source": "regular_pizza.png",
            "sizes": RegularPizza.objects.filter(pizza_type=item_type).values_list('size', flat=True).distinct(),
            "num_toppings": RegularPizza.objects.filter(pizza_type=item_type).values_list('num_toppings', flat=True).distinct(),
            "available_toppings": PizzaTopping.objects.all()
        }
        return render(request, "orders/product.html", context)

    elif product_type=="Sicilian Pizza":
        if item_type not in SicilianPizza.objects.values_list('pizza_type', flat=True).distinct():
            return render(request, "orders/error.html", {"error": "Invalid Product"})
        context = {
            "product_type": product_type,
            "item_type": item_type,
            "product": item_type + " Pizza",
            "image_source": "sicilian_pizza.png",
            "sizes": SicilianPizza.objects.filter(pizza_type=item_type).values_list('size', flat=True).distinct(),
            "num_toppings": SicilianPizza.objects.filter(pizza_type=item_type).values_list('num_toppings', flat=True).distinct(),
            "available_toppings": PizzaTopping.objects.all()
        }
        return render(request, "orders/product.html", context)
    elif product_type=="Sub":
        if item_type not in Sub.objects.values_list('sub_type', flat=True).distinct():
            return render(request, "orders/error.html", {"error": "Invalid Product"})
        context = {
            "product_type": product_type,
            "item_type": item_type,
            "product": item_type + " Sub",
            "image_source": "sandwich.png",
            "sizes": Sub.objects.filter(sub_type=item_type).values_list('size', flat=True).distinct()
        }
        return render(request, "orders/product.html", context)   
    elif product_type=="Pasta":
        if item_type not in Pasta.objects.values_list('pasta_type', flat=True).distinct():
            return render(request, "orders/error.html", {"error": "Invalid Product"})
        context = {
            "product_type": product_type,
            "item_type": item_type,
            "product": item_type + " Pasta",
            "image_source": "pasta.png"
        }
        return render(request, "orders/product.html", context)
    elif product_type=="Salad":
        if item_type not in Salad.objects.values_list('salad_type', flat=True).distinct():
            return render(request, "orders/error.html", {"error": "Invalid Product"})
        context = {
            "product_type": product_type,
            "item_type": item_type,
            "product": item_type + " Salad",
            "image_source": "salad.png"
        }
        return render(request, "orders/product.html", context)
    elif product_type=="Dinner Platter":
        if item_type not in DinnerPlatter.objects.values_list('dinner_platter_type', flat=True).distinct():
            return render(request, "orders/error.html", {"error": "Invalid Product"})
        context = {
            "product_type": product_type,
            "item_type": item_type,
            "product": item_type + " Platter",
            "image_source": "dinner_platter.png",
            "sizes": DinnerPlatter.objects.filter(dinner_platter_type=item_type).values_list('size', flat=True).distinct()
        }
        return render(request, "orders/product.html", context)
    else:
        return render(request, "orders/error.html", {"error": "Invalid Product"})


@csrf_exempt
def get_cost(request):
    if request.method =="GET":
        return render(request, "orders/error.html", {"error": "Invalid Access"})
    
    product_type = request.POST["product_type"]
    product = request.POST["product"]
    size = request.POST["size"]

    if product_type=="Regular Pizza":
        if product=="Cheese":
            item = RegularPizza.objects.get(pizza_type=product, size=size)
        else:
            num_toppings = request.POST["num_toppings"]
            item = RegularPizza.objects.get(pizza_type=product, size=size, num_toppings=num_toppings)

    elif product_type=="Sicilian Pizza":
        if product=="Cheese":
            item = SicilianPizza.objects.get(pizza_type=product, size=size)
        else:
            num_toppings = request.POST["num_toppings"]
            item = SicilianPizza.objects.get(pizza_type=product, size=size, num_toppings=num_toppings)
    
    elif product_type=="Sub":
        item = Sub.objects.get(sub_type=product, size=size)
    elif product_type=="Pasta":
        item = Pasta.objects.get(pasta_type=product)
    elif product_type=="Salad":
        item = Salad.objects.get(salad_type=product)
    elif product_type=="Dinner Platter":
        item = DinnerPlatter.objects.get(dinner_platter_type=product, size=size)
    else:
        return JsonResponse({'success': False})

    if item is None:
        return JsonResponse({'success': False})
    
    return JsonResponse({'success': True, 'cost': item.cost})

@login_required(login_url="/login")
def add_to_cart(request, product_type, item_type):    
    if request.method=="GET":
        return render(request, "orders/error.html", {"error": "Invalid access"})
    
    try:
        user = User.objects.get(username=request.user)
        if product_type=="Regular Pizza":
            size = request.POST["size"]
            if item_type=="Cheese":
                cost = RegularPizza.objects.get(pizza_type=item_type, size=size).cost
                order = Orders(user=user, product_type=product_type, item_type=item_type, size=size, cost=cost)
                order.save()
            else:
                num_toppings = int(request.POST["num_toppings"])
                toppings_select = request.POST.getlist("toppings_select")
                
                if num_toppings != len(toppings_select):
                    return render(request, "orders/error.html", {"error": "Invalid request"})
                cost = RegularPizza.objects.get(pizza_type=item_type, size=size, num_toppings=num_toppings).cost
                order = Orders(user=user, product_type=product_type, item_type=item_type, size=size, cost=cost, num_toppings=num_toppings)
                order.save()
                for i in toppings_select:
                    topping = PizzaTopping.objects.get(topping=i)
                    order.pizza_toppings.add(topping)

        elif product_type=="Sicilian Pizza":
            size = request.POST["size"]
            if item_type=="Cheese":
                cost = SicilianPizza.objects.get(pizza_type=item_type, size=size).cost
                order = Orders(user=user, product_type=product_type, item_type=item_type, size=size, cost=cost)
                order.save()
            else:
                num_toppings = int(request.POST["num_toppings"])
                toppings_select = request.POST.getlist("toppings_select")
                
                if num_toppings != len(toppings_select):
                    return render(request, "orders/error.html", {"error": "Invalid request"})
                cost = SicilianPizza.objects.get(pizza_type=item_type, size=size, num_toppings=num_toppings).cost
                order = Orders(user=user, product_type=product_type, item_type=item_type, size=size, cost=cost, num_toppings=num_toppings)
                order.save()
                for i in toppings_select:
                    topping = PizzaTopping.objects.get(topping=i)
                    order.pizza_toppings.add(topping)
        
        elif product_type=="Sub":
            size = request.POST["size"]
            cost = Sub.objects.get(sub_type=item_type, size=size).cost
            order = Orders(user=user, product_type=product_type, item_type=item_type, size=size, cost=cost)
            order.save()
        elif product_type=="Pasta":
            cost = Pasta.objects.get(pasta_type=item_type).cost
            order = Orders(user=user, product_type=product_type, item_type=item_type, cost=cost)
            order.save()
        elif product_type=="Salad":
            cost = Salad.objects.get(salad_type=item_type).cost
            order = Orders(user=user, product_type=product_type, item_type=item_type, cost=cost)
            order.save()
        elif product_type=="Dinner Platter":
            size = request.POST["size"]
            cost = DinnerPlatter.objects.get(dinner_platter_type=item_type, size=size).cost
            order = Orders(user=user, product_type=product_type, item_type=item_type, size=size, cost=cost)
            order.save()
        else:
            return render(request, "orders/error.html", {"error": "Invalid access"})
    except:
        return render(request, "orders/error.html", {"error": "Invalid access"})

    return HttpResponseRedirect(reverse("index"))

@login_required(login_url="/login")
def cart_view(request):
    user = User.objects.get(username=request.user)
    cart_orders = Orders.objects.filter(user=user, order_placed=False)
    total_cost = 0
    for order in cart_orders:
        total_cost += order.cost
    return render(request, "orders/cart.html", {"cart_orders": cart_orders, "total_cost":total_cost})

@login_required(login_url="/login")
def clear_cart(request):
    user = User.objects.get(username=request.user)
    Orders.objects.filter(user=user, order_placed=False).delete()
    return HttpResponseRedirect(reverse("cart"))

@login_required(login_url="/login")
def submit_orders(request):
    user = User.objects.get(username=request.user)
    cart_orders = Orders.objects.filter(user=user, order_placed=False)
    for order in cart_orders:
        order.order_placed = True
        order.save()
        a_o = ActiveOrders(order=order)
        a_o.save()
    return render(request, "orders/success.html", {"message": "Order Successfully Placed"})

@login_required(login_url="/login")
def order_history_view(request):
    user = User.objects.get(username=request.user)
    # Get most recent orders first
    orders = Orders.objects.filter(user=user, order_placed=True).order_by("-pk")
    return render(request, "orders/all_orders.html", {"orders": orders})

def register_view(request):
    if request.method == "GET":
        return render(request, "orders/register.html")

    if request.user.is_authenticated:
        return render(request, "orders/error.html", {"error": "User Already Logged In"})
    if not request.POST["first_name"]:
        return render(request, "orders/error.html", {"error": "No First Name Entered"})
    if not request.POST["last_name"]:
        return render(request, "orders/error.html", {"error": "No Last Name Entered"})
    if not request.POST["email"]:
        return render(request, "orders/error.html", {"error": "No E-mail Entered"})
    if not request.POST["username"]:
        return render(request, "orders/error.html", {"error": "No Username Entered"})
    if not request.POST["password"]:
        return render(request, "orders/error.html", {"error": "No Password Entered"})
    if not request.POST["confirm_password"]:
        return render(request, "orders/error.html", {"error": "No Confirmation Password Entered"})
    if request.POST["password"] != request.POST["confirm_password"]:
        return render(request, "orders/error.html", {"error": "Password and Confirmation Password Don't Match"})
    
    user = User.objects.create_user(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], username=request.POST["username"], password=request.POST["password"])
    user.save()
    user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
    login(request, user)
    return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "GET":
        return render(request, "orders/login.html")

    if request.user.is_authenticated:
        return render(request, "orders/error.html", {"error": "User Already Logged In"})
    if not request.POST["username"]:
        return render(request, "orders/error.html", {"error": "No Username Entered"})
    if not request.POST["password"]:
        return render(request, "orders/error.html", {"error": "No Password Entered"})
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/error.html", {"error": "Invalid credentials"})

def logout_view(request):
    if not request.user.is_authenticated:
        return render(request, "orders/error.html", {"error": "User Not Logged In, No User To Log Out"})
    else:
        logout(request)
        return HttpResponseRedirect(reverse("index"))
