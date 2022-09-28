import json
import os


class ProductModel:
    def __init__(self, id, product_name, quantity, price):
        self.id = id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

    # add new product
    @classmethod
    def add_product(cls, product_name, quantity, price):
        from Controllers.productMenu import product_menu
        f = open('Files/products_file.json', 'r')

        if os.stat('Files/products_file.json').st_size == 0:
            products = []
            product_id = 1
        else:
            products = json.load(f)
            product_id = int(products[-1].get("id")) + 1

        product = {
            "id": product_id,
            "product_name": product_name,
            "quantity": quantity,
            "price": price
        }
        products.append(product)

        with open('Files/products_file.json', 'w', encoding='utf-8') as json_file:
            json.dump(products, json_file, indent=4, separators=(',', ': '))

        print('Product Added Successfully!')
        product_menu()

    # fetch all products
    @classmethod
    def fetch_all_products(cls):
        file = open('Files/products_file.json', 'r')
        if os.stat('Files/products_file.json').st_size == 0:
            products = []
        else:
            products = json.load(file)
        return products

    # fetch product by id
    @classmethod
    def fetch_product_by_id(cls, id):
        product = []
        file = open('Files/products_file.json', 'r')
        if os.stat('Files/products_file.json').st_size == 0:
            product = []
        else:
            products = json.load(file)
            for each in products:
                if each.get("id") == id:
                    product = each
        return product

    # check whether product exists
    @classmethod
    def check_product_exists(cls, product_name):
        exists_status = False
        file = open('Files/products_file.json', 'r')
        if os.stat('Files/products_file.json').st_size == 0:
            exists_status = False
        else:
            products = json.load(file)
            for each in products:
                if each.get("product_name") == product_name:
                    exists_status = True
        return exists_status

    # check whether id exists
    @classmethod
    def check_id_exists(cls, id):
        exists_status = False
        file = open('Files/products_file.json', 'r')
        if os.stat('Files/products_file.json').st_size == 0:
            exists_status = False
        else:
            products = json.load(file)
            for each in products:
                if each.get("id") == id:
                    exists_status = True
        return exists_status

    # update product by id
    @classmethod
    def update_product_by_id(self, id, product_name, quantity, price):
        f = open('Files/products_file.json', 'r')
        products = json.load(f)

        for product in products:
            if product.get("id") == id:
                product.update({
                    "id": id,
                    "product_name": product_name,
                    "quantity": quantity,
                    "price": price
                })

        with open('Files/products_file.json', 'w', encoding='utf-8') as json_file:
            json.dump(products, json_file, indent=4, separators=(',', ': '))

    # delete product by id
    @classmethod
    def delete_product_by_id(cls, id):
        f = open('Files/products_file.json', 'r')
        products = json.load(f)

        for product in products:
            if product.get("id") == id:
                products.pop(products.index(product))

        with open('Files/products_file.json', 'w', encoding='utf-8') as json_file:
            json.dump(products, json_file, indent=4, separators=(',', ': '))
