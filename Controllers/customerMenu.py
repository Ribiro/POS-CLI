from Models.customers import CustomerModel


def customer_menu_queries():
    print('***Customer Operations***')

    # these print statements provides the user with the available options to choose from
    print('\t1. Add New Customer')
    print('\t2. Delete Customer Details')
    print('\t3. Update Customer Details')
    print('\t0. Go Back to Main Menu')


def customer_menu():
    from Controllers.mainMenu import main_menu
    customer_menu_queries()

    # take user choice
    user_choice = input('Please enter your choice to proceed: ')

    while True:
        if user_choice == '1':
            id = input("\tEnter Customer ID: ")
            first_name = input("\tEnter Customer First Name: ")
            last_name = input("\tEnter Customer Last Name: ")
            phone_number = input("\tEnter Customer Phone Number: ")
            CustomerModel.add_customer(id=id, first_name=first_name, last_name=last_name, phone_number=phone_number)
        elif user_choice == '2':
            pass
        elif user_choice == '3':
            pass
        elif user_choice == '0':
            main_menu()
        else:
            print('Warning! Wrong choice.')
            main_menu()
