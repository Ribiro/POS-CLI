from Models.products import ProductModel
from Models.customers import CustomerModel
import os
import json


def purchase_product():
    from Controllers.mainMenu import main_menu
    customer_id = int(input('Enter ID of customer purchasing a product: '))
    if CustomerModel.check_id_exists(customer_id):
        product_id = int(input('Enter ID of product you wish to purchase: '))
        if ProductModel.check_id_exists(product_id):
            product_to_buy = ProductModel.fetch_product_by_id(product_id).get("product_name")
            quantity = int(input('Enter quantity of ' + str(product_to_buy) + ' to buy: '))
            price = ProductModel.fetch_product_by_id(product_id).get("price")
            amount_spent = price * quantity

            f = open('Files/purchases.json', 'r')
            if os.stat('Files/purchases.json').st_size == 0:
                purchases = []
                purchase_id = 1
            else:
                purchases = json.load(f)
                purchase_id = int(purchases[-1].get("id")) + 1

            # the purchase
            purchase = {
                "id": purchase_id,
                "product_name": product_to_buy,
                "quantity": quantity,
                "amount_spent": amount_spent,
                "customer_id": customer_id
            }

            purchases.append(purchase)

            # check whether quantity is less than or equal to available product quantity
            if  ProductModel.fetch_product_by_id(product_id).get("quantity") >= purchase.get("quantity"):
                if ProductModel.fetch_product_by_id(product_id).get("id"):
                    # write to purchases file
                    with open('Files/purchases.json', 'w', encoding='utf-8') as json_file:
                        json.dump(purchases, json_file, indent=4, separators=(',', ': '))

                    # remove bought quantity
                    product_name = ProductModel.fetch_product_by_id(product_id).get("product_name")
                    remaining_quantity = ProductModel.fetch_product_by_id(product_id).get("quantity") - quantity
                    ProductModel.update_product_by_id(id=product_id, product_name=product_name, quantity=remaining_quantity,
                                                      price=price)
                    print('Purchase Completed Successfully!')
                    main_menu()
            else:
                print('Cant purchase product! Insufficient quantity')
                main_menu()
        else:
            print('Product with this ID does not exist!')
            main_menu()
    else:
        print("Customer with this ID does not exist!")
        main_menu()
