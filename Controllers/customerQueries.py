from Models.customers import CustomerModel
import os
import json


def queries_options():
    print('***Customers Queries***')

    # these print statements provides the user with the available options to choose from
    print('\t1. Search for a customer using ID')
    print('\t2. List all customers')
    print('\t3. Search for customer and their purchase history (using phone number)')
    print('\t0. Go Back to Main Menu')


def customer_queries():
    from Controllers.mainMenu import main_menu
    queries_options()

    # take user choice
    user_choice = input('Please enter your choice to proceed: ')

    while True:
        # choice 1 searches for a customer (using ID for this case)
        if user_choice == '1':
            customer_id = int(input('Enter customer ID for the customer you wish to search: '))

            if CustomerModel.check_id_exists(customer_id):
                the_customer = CustomerModel.fetch_customer_by_id(customer_id)

                print('****Customer****')
                print('ID:' + str(the_customer.get('id')) + ' | Full Name: ' + str(the_customer.get('first_name')) + ' ' +
                      str(the_customer.get('last_name')) + ' | Phone Number: ' + str(the_customer.get('phone_number')))
                main_menu()
            else:
                print('Cant find a customer with this search ID!')
                main_menu()

        # choice 2 lists all the customers
        elif user_choice == '2':
            all_customers = CustomerModel.fetch_all_customers()
            # print('Your search result is: ' + str(all_customers))
            print('********Customers*********')
            for customer in all_customers:
                print('ID:' + str(customer.get('id')) + ' | Full Name: ' + str(
                    customer.get('first_name')) + ' ' +
                      str(customer.get('last_name')) + ' | Phone Number: ' + str(customer.get('phone_number')))
            main_menu()

        # search for a customer and their search history
        elif user_choice == '3':
            phone_number = input('Enter customer phone number for the customer you wish to search history: ')

            if CustomerModel.check_phone_number_exists(phone_number):
                the_customer = CustomerModel.fetch_customer_by_phone_number(phone_number)
                print('Customer Name: ' + str(the_customer.get('first_name')) + ' ' + str(the_customer.get('last_name')))

                # purchase history
                purchase_history = []
                f = open('Files/purchases.json', 'r')
                if os.stat('Files/customers_file.json').st_size == 0:
                    print('Purchase History for this Customer is Empty!')
                    main_menu()
                else:
                    purchases = json.load(f)
                    for history in purchases:
                        if history.get("customer_id") == the_customer.get("id"):
                            purchase_history.append(history)

                    if len(purchase_history) == 0:
                        print('Purchase History for this Customer is Empty!')
                        main_menu()
                    else:
                        print('Purchase History')
                        print('*****************************')
                        for item in purchase_history:
                            print('ID: ' + str(item.get('id')) + '||' + 'Product: ' + str(item.get('product_name')) + '||' +
                                  'Amount Spent: ' + str(item.get('amount_spent')))
                        main_menu()
            else:
                print('Cant find a customer with this search phone number!')
                main_menu()

        # choice 0 takes us back to main menu
        elif user_choice == '0':
            main_menu()

        # Invalid choice takes us back to main menu
        else:
            print('Warning! Wrong choice.')
            main_menu()
