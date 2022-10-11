# POS-CLI
## Overview
POS-CLI is a command line customer-product PoS system based on customers, products, 
and the purchases made by the customers. The main aim of this project is to implement a python program
that presents the user with a menu, gets the user's choice, and processes the given options.

This program will assist in managing customer and product data in the system and enable 
customers to make purchases of the products in stock. Therefore, the program will allow the user 
to create a new customer, update the customer information, search for a customer, and delete a 
customer from the system. Additionally, the user can add new products, edit 
existing products, explore the products, and delete products. Finally, purchases can be made with the 
customer IDs and product IDs in the system.

**Language Used:** Python

## Table of Contents
* [Customer Operations](#customer-operations)
* [Product Operations](#product-operations)
* [Purchase Operations](#purchase-operations)
* [Setup](#setup)

<a name="customer-operations"></a>
## Customer Operations
Customer operations are the first option in this program's main menu. In this section, the user can add
new customer details, delete customer details, update customer details, or perform basic 
customer query operations. In the query operations, the user can fetch all customers or a single
customer details, including their purchase history, using either customer ID or Phone Number, which
are both unique.

Customers details are stored in <a href="https://github.com/Ribiro/POS-CLI/blob/main/Files/customers_file.json">customers_file.json</a>.

<a name="product-operations"></a>
## Product Operations
Product operations are the second option in this program's main menu. Similarly, the user can add
new product details, delete, update product details, or perform basic 
product query operations in this section. In the query operations, the user can fetch all products or single
product details using the product ID, which is unique.

Products details are stored in <a href="https://github.com/Ribiro/POS-CLI/blob/main/Files/products_file.json">products_file.json</a>.

<a name="purchase-operations"></a>
## Purchase Operations
Purchase operations are the last option before quitting, allowing one to exit the program.
To make a purchase, the user must provide a valid customer ID. If the customer ID does not 
exist, they are taken to the main menu, and an error message is printed.

If the customer ID is valid, a valid product ID will be required to proceed with the purchase.
The program checks whether the quantity to purchase exceeds the amount in stock, upon which the user
is prompted with an error message and required to lower the amount.

One can buy multiple products at the same time. A receipt that includes products purchased
and the total amount is generated upon checkout, and the stock is updated accordingly.

Purchase details are stored in <a href="https://github.com/Ribiro/POS-CLI/blob/main/Files/purchases.json">purchases.json</a>.

<a name="setup"></a>
## Setup
To run this project, clone it to your local machine and execute the following commands:

```angular2html
$ git clone https://github.com/Ribiro/POS-CLI.git
$ cd POS-CLI
$ pip install -r requirements.txt
$ python main.py
```

