from Models.customers import CustomerModel


def customer_menu_queries():
    print('***Customer Operations***')

    # these print statements provides the user with the available options to choose from
    print('\t1. Add New Customer')
    print('\t2. Delete Customer Details')
    print('\t3. Update Customer Details')
    print('\t4. Customer Queries')
    print('\t0. Go Back to Main Menu')


def customer_menu():
    from Controllers.mainMenu import main_menu
    from Controllers.customerQueries import customer_queries
    customer_menu_queries()

    # take user choice
    user_choice = input('Please enter your choice to proceed: ')

    while True:
        # choice 1 adds a new customer
        if user_choice == '1':
            first_name = input("\tEnter Customer First Name: ")
            last_name = input("\tEnter Customer Last Name: ")
            phone_number = input("\tEnter Customer Phone Number: ")
            email = input("\tEnter Email: ")
            if CustomerModel.check_phone_number_exists(phone_number):
                if CustomerModel.check_email_exists(email):
                    print('Customer with this phone number/email already exists!')
                    main_menu()
            else:
                CustomerModel.add_customer(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email)

        # choice 2 deletes a customer
        elif user_choice == '2':
            id = int(input("To proceed, enter the ID of the customer to delete: "))
            if CustomerModel.check_id_exists(id):
                CustomerModel.delete_customer_by_id(id)
                print('Customer deleted successfully!')
                main_menu()
            else:
                print('Customer with this ID does not exist!')
                main_menu()

        # choice 3 updates a customer
        elif user_choice == '3':
            id = int(input("To proceed, enter the ID of the customer to update: "))
            if CustomerModel.check_id_exists(id):
                first_name = input("\tEnter New Customer First Name: ")
                last_name = input("\tEnter New Customer Last Name: ")
                phone_number = input("\tEnter New Customer Phone Number: ")
                email = input("\tEnter Email: ")
                CustomerModel.update_customer_by_id(id=id, first_name=first_name, last_name=last_name,
                                                    phone_number=phone_number, email=email)
                print("Customer Details Updated Successfully!")
                main_menu()
            else:
                print("Customer with this ID does not exist!")
                main_menu()

        # choice 4 performs the customers queries
        elif user_choice == '4':
            customer_queries()

        # choice 0 takes us back to main menu
        elif user_choice == '0':
            main_menu()

        # Invalid choice takes us back to main menu
        else:
            print('Warning! Wrong choice.')
            main_menu()
