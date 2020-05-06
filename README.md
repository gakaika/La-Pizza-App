# La Pizza App

A pizza and subs restaurant online ordering application wherein customers can view the menu and prices, add items in their cart, and place orders intended for pickup and payment later. Following this, the restaurant staff or owner can view all active orders in the adminstrator interface and update the status accordingly. 

This web application is built with **Django** in Python and **Javascript**.

## Built With
* **Django** used for server-side management
* **SQLite 3** for database storage of users, menu items, items in cart, active orders, and more
* **Bootstrap 4** used for styling web pages, along with custom **CSS** code
* **Javascript** used for enhancing the user experience when browsing the menu items with the following functionality:
  * **AJAX** with **XML Http Requests** used to dynamically fetch the updated cost from the server whenever the user changes the product's attributes such as pizza toppings, size, etc.
  * Other functionality such as only allowing the user to select the number of toppings specified, allowing form submissions only when all relevent criteria inputted for a product, and updating cost with AJAX when product attributes changed.

## Features
* Powerful adminstrator user interface to manage product collection and customizations, as well as track active orders and update their status on the SQLite database
* Intuitive and easy to use interface for customers with easy viewing of products on menu, customizing products, saving items in carts and placing an order
* Allows users to check the status of their orders once placed
* Strong error management checks on both client and server side

## Setup and Usage
First create a super-user to manage the application's database, which will have access to the product collection and active orders for fulfillment. Simply run the below command inside the folder for this application, and follow the prompts:

    python manage.py createsuperuser

After this, the application can be run by:

    python manage.py runserver

To access the adminstrator user interface, simply go to the **/admin** route. Please look at the demo video on how to use this to track orders, update their status, and managing the product collection.

## Credits
Restaurant menu inspired from [Pinocchio's Pizza and Subs](http://www.pinocchiospizza.net/menu.html)
