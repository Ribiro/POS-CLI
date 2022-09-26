from Controllers import customerMenu
from Controllers import productMenu


def main_menu_queries():
    print('***POS CLI***')

    # these print statements provides the user with the available options to choose from
    print('\t1. Customer Operations')
    print('\t2. Product Operations')
    print('\t3. Purchase Operations')
    print('\t0. Quit')


def main_menu():
    main_menu_queries()

    # take user choice
    user_choice = input('Please enter your choice to proceed: ')

    while True:
        if user_choice == '1':
            customerMenu.customer_menu()
        elif user_choice == '2':
            productMenu.product_menu()
        elif user_choice == '3':
            pass
        elif user_choice == '0':
            print('POS CLI Exited!')
            quit()
        else:
            print('Warning! Wrong choice.')
