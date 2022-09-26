def product_menu_queries():
    print('***Product Operations***')

    # these print statements provides the user with the available options to choose from
    print('1. Add New Product')
    print('2. Delete Product Details')
    print('3. Update Product Details')
    print('0. Go Back to Main Menu')


def product_menu():
    from Controllers.mainMenu import main_menu
    product_menu_queries()

    # take user choice
    user_choice = input('Please enter your choice to proceed: ')

    while True:
        if user_choice == '1':
            pass
        elif user_choice == '2':
            pass
        elif user_choice == '3':
            pass
        elif user_choice == '0':
            main_menu()
        else:
            print('Warning! Wrong choice.')
            main_menu()
