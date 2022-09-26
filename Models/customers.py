import json
import os


class CustomerModel:
    def __init__(self, id, first_name, last_name, phone_number):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    # add new customer details
    @classmethod
    def add_customer(cls, id, first_name, last_name, phone_number):
        from Controllers.customerMenu import customer_menu
        f = open('Files/customers_file.json', 'r')

        if os.stat('Files/customers_file.json').st_size == 0:
            names = []
        else:
            names = json.load(f)

        customer = {
            "id": id,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number
        }

        names.append(customer)

        with open('Files/customers_file.json', 'w', encoding='utf-8') as json_file:
            json.dump(names, json_file, indent=4, separators=(',', ': '))

        print('Customer Added Successfully!')
        customer_menu()
