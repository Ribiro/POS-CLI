from Controllers.customerMenu import customer_menu
from Controllers.productMenu import product_menu


def main_menu_queries():
    print('***Welcome to POS CLI***')

    # these print statements provides the user with the available options to choose from
    print('1. Customer Operations')
    print('2. Product Operations')
    print('3. Purchase Operations')
    print('0. Quit')


def main_menu():
    main_menu_queries()

    # take user choice
    user_choice = input('Please enter your choice to proceed: ')

    while True:
        if user_choice == '1':
            customer_menu()
        elif user_choice == '2':
            product_menu()
        elif user_choice == '3':
            pass
        elif user_choice == '0':
            print('POS CLI Exited!')
            quit()
        else:
            print('Warning! Wrong choice.')
