import json
import os


class CustomerModel:
    def __init__(self, id, first_name, last_name, phone_number):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    # add new customer details
    @classmethod  # binds this method to the class, and not the object of the class
    def add_customer(cls, first_name, last_name, phone_number):
        from Controllers.customerMenu import customer_menu
        f = open('Files/customers_file.json', 'r')

        if os.stat('Files/customers_file.json').st_size == 0:
            names = []
            customer_id = 1
        else:
            names = json.load(f)
            customer_id = int(names[-1].get("id")) + 1

        customer = {
            "id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number
        }

        names.append(customer)

        with open('Files/customers_file.json', 'w', encoding='utf-8') as json_file:
            json.dump(names, json_file, indent=4, separators=(',', ': '))

        print('Customer Added Successfully!')
        customer_menu()

    # fetch all customers
    @classmethod
    def fetch_all_customers(cls):
        file = open('Files/customers_file.json', 'r')
        if os.stat('Files/customers_file.json').st_size == 0:
            customers = []
        else:
            customers = json.load(file)
        return customers

    # fetch customer by id
    @classmethod
    def fetch_customer_by_id(cls, id):
        customer = []
        file = open('Files/customers_file.json', 'r')
        if os.stat('Files/customers_file.json').st_size == 0:
            customer = []
        else:
            customers = json.load(file)
            for each in customers:
                if each.get("id") == id:
                    customer = each
        return customer

    # fetch customer using phone number
    @classmethod
    def fetch_customer_by_phone_number(cls, phone_number):
        customer = []
        file = open('Files/customers_file.json', 'r')
        if os.stat('Files/customers_file.json').st_size == 0:
            customer = []
        else:
            customers = json.load(file)
            for each in customers:
                if each.get("phone_number") == phone_number:
                    customer = each
        return customer

    # check whether phone number exists
    @classmethod
    def check_phone_number_exists(cls, phone_number):
        exists_status = False
        file = open('Files/customers_file.json', 'r')
        if os.stat('Files/customers_file.json').st_size == 0:
            exists_status = False
        else:
            customers = json.load(file)
            for each in customers:
                if each.get("phone_number") == phone_number:
                    exists_status = True
        return exists_status

    # check whether id exists
    @classmethod
    def check_id_exists(cls, id):
        exists_status = False
        file = open('Files/customers_file.json', 'r')
        if os.stat('Files/customers_file.json').st_size == 0:
            exists_status = False
        else:
            customers = json.load(file)
            for each in customers:
                if each.get("id") == id:
                    exists_status = True
        return exists_status

    # update customer by id
    @classmethod
    def update_customer_by_id(self, id, first_name, last_name, phone_number):
        f = open('Files/customers_file.json', 'r')
        customers = json.load(f)

        for customer in customers:
            if customer.get("id") == id:
                customer.update({
                    "id": id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number
                })

        with open('Files/customers_file.json', 'w', encoding='utf-8') as json_file:
            json.dump(customers, json_file, indent=4, separators=(',', ': '))

    # delete customer by id
    @classmethod
    def delete_customer_by_id(cls, id):
        f = open('Files/customers_file.json', 'r')
        customers = json.load(f)

        for customer in customers:
            if customer.get("id") == id:
                customers.pop(customers.index(customer))

        with open('Files/customers_file.json', 'w', encoding='utf-8') as json_file:
            json.dump(customers, json_file, indent=4, separators=(',', ': '))
