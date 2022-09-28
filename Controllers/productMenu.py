from Models.products import ProductModel


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
        # choice 1 adds a new product
        if user_choice == '1':
            product_name = input("\tEnter Name of Product: ")
            quantity = int(input("\tEnter Quantity of Product: "))
            if ProductModel.check_product_exists(product_name):
                print('Product with this name already exists!')
                main_menu()
            else:
                ProductModel.add_product(product_name=product_name, quantity=quantity)
                print('Product added successfully!')
                main_menu()

        # choice 2 deletes a product
        elif user_choice == '2':
            id = int(input("To proceed, enter the ID of the product to delete: "))
            if ProductModel.check_id_exists(id):
                ProductModel.delete_product_by_id(id)
                print('Product deleted successfully!')
                main_menu()
            else:
                print('Product with this ID does not exist!')
                main_menu()

        # choice 3 updates a product
        elif user_choice == '3':
            id = int(input("To proceed, enter the ID of the product to update: "))
            if ProductModel.check_id_exists(id):
                product_name = input("\tEnter New Name of Product: ")
                quantity = int(input("\tEnter New Quantity of Product: "))
                ProductModel.update_product_by_id(id=id, product_name=product_name, quantity=quantity)
                print("Product Details Updated Successfully!")
                main_menu()
            else:
                print("Product with this ID does not exist!")
                main_menu()

        # choice 0 takes us back to main menu
        elif user_choice == '0':
            main_menu()

        # Invalid choice takes us back to main menu
        else:
            print('Warning! Wrong choice.')
            main_menu()
