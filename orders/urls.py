from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("item/<str:product_type>/<str:item_type>/", views.product_view, name="product"),
    path("item/getcost", views.get_cost, name="getcost"),
    path("item/<str:product_type>/<str:item_type>/cart/add", views.add_to_cart, name="add_to_cart"),
    path("cart", views.cart_view, name="cart"),
    path("cart/clear", views.clear_cart, name="clear_cart"),
    path("cart/orders/submit", views.submit_orders, name="submit_orders"),
    path("orders/all", views.order_history_view, name="order_history"),
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]
