from Models.products import ProductModel


def queries_options():
    print('***Products Queries***')

    # these print statements provides the user with the available options to choose from
    print('\t1. Search for a product by ID')
    print('\t2. Search for a product by name')
    print('\t3. List all products')
    print('\t0. Go Back to Main Menu')


def product_queries():
    from Controllers.mainMenu import main_menu
    queries_options()

    # take user choice
    user_choice = input('Please enter your choice to proceed: ')

    while True:
        # choice 1 searches for a product (using ID)
        if user_choice == '1':
            product_id = int(input('Enter product ID for the product you wish to search: '))

            if ProductModel.check_id_exists(product_id):
                the_product = ProductModel.fetch_product_by_id(product_id)

                print('****Product****')
                print('ID:' + str(the_product.get('id')) + ' | Product Name: ' + str(the_product.get('product_name')) +
                      ' | Quantity: ' + str(the_product.get('quantity')))
                main_menu()
            else:
                print('Cant find product with this search ID!')
                main_menu()

        # choice 2 searches for a product (using name)
        elif user_choice == '2':
            product_name = input('Enter name of the product you wish to search: ')

            if ProductModel.check_product_exists(product_name):
                the_product = ProductModel.fetch_product_by_name(product_name)

                print('****Product****')
                print('ID:' + str(the_product.get('id')) + ' | Product Name: ' + str(the_product.get('product_name')) +
                      ' | Quantity: ' + str(the_product.get('quantity')))
                main_menu()
            else:
                print('Cant find product with this search name!')
                main_menu()

        # choice 3 lists all the products
        elif user_choice == '3':
            all_products = ProductModel.fetch_all_products()
            print("********Products*********")
            for product in all_products:
                print('ID:' + str(product.get('id')) + ' | Product Name: ' + str(product.get('product_name')) +
                      ' | Quantity: ' + str(product.get('quantity')))
            main_menu()

        # choice 0 takes us back to main menu
        elif user_choice == '0':
            main_menu()

        # Invalid choice takes us back to main menu
        else:
            print('Warning! Wrong choice.')
            main_menu()
