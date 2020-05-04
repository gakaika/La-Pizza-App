# La Pizza App

A pizza and subs restaurant online ordering application wherein customers can view the menu and prices, add items in their cart, and place orders intended for pickup and payment later. Following this, the restaurant staff or owner can view all active orders in the adminstrator interface and update the status accordingly. 

This web application is built with Django in Python and Javascript.

## Built With
* **Django** used for server-side management
* **SQLite 3** for database storage of users, menu items, items in cart, active orders, and more
* **Bootstrap 4** used for styling web pages, along with custom **CSS** code
* **Javascript** used for enhancing the user experience when browsing the menu items with the following functionality:
  * **AJAX** with **XML Http Requests** used to dynamically fetch the updated cost from the server whenever the user changes the product's attributes such as pizza toppings, size, etc.
  * Other functionality such as only allowing the user to select the number of toppings specified, allowing form submissions only when all relevent criteria inputted for a product, and updating cost with AJAX when product attributes changed.

## Features
* Powerful adminstrator user interface to manage product collection, active orders, and product customizations on the SQLite database
* Intuitive and easy to use interface for customers with easy viewing of products on menu, customizing products, saving items in carts and placing an order
