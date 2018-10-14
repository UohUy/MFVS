class UI:
    @staticmethod
    def homepage():
        print('--------MFVS--------')
        print('Login with:')
        print('1. Customer Account')
        print('2. Owner Account')
        print('3. Create Customer Account')
        print('9. Exit')

    @staticmethod
    def customer_homepage():
        print('--------MFVS--------')
        print('1. View Product')
        print('2. Search Product')
        print('3. Sort Product')
        print('4. Check Cart')
        print('5. Check My Order')
        print('6. Modify Account')
        print('7. Delete Account')
        print('9. Exit')

    @staticmethod
    def view_product(products):
        print('--------View Product--------')
        for i in range(len(products)):
            print('{}. {}'.format(i + 1, products[i].name))
        print('7. Previous Page')
        print('8. Next Page')
        print('9. Back to Home Page')

    @staticmethod
    def view_product_detail_by_customer(product):
        print('--------View Product Detail--------')
        print(product)
        print('1. Add to Cart')
        print('2. Back to Previous Page')
        print('9. Exit')

    @staticmethod
    def sort_product():
        print('--------Sort Product--------')
        print('1. Sort by Name(Ascending Order)')
        print('2. Sort by Name(Descending Order')
        print('3. Sort by Price(Low to High')
        print('4. Sort by Price(High to Low')

    @staticmethod
    def modify_customer_account():
        print('--------Modify Customer Account--------')
        print('1. Edit Username')
        print('2. Edit Password')
        print('3. Back to Previous Page')
        print('9. Exit')

    @staticmethod
    def edit_username():
        print('--------Edit Username--------')

    @staticmethod
    def edit_password():
        print('--------Edit Password--------')

    @staticmethod
    def password_valid_information():
        print('Password needs contain at least:'
              '\n\t- one upper case letter;'
              '\n\t- one lower case letter'
              '\n\t- one number'
              '\n\t- one special character'
              '\nAnd length has to longer than 8 characters')

    @staticmethod
    def check_cart(cart):
        print('--------Check Cart--------')
        i = 0
        for product, info in cart:
            print('{}. {}: {} {}'.format(i, product.name, info[0], info[1]))
            i += 1
        print('6. Clear Cart')
        print('7. Edit Cart')
        print('8. Generate Order')
        print('9. Go back to previous page')

    @staticmethod
    def edit_cart(cart):
        print('--------Edit Cart--------')
        i = 0
        for product, info in cart:
            print('{}. {}: {} {}'.format(i, product.name, info[0], info[1]))
            i += 1
        print('9. Go back to previous page')

    @staticmethod
    def edit_product_in_cart(product, info):
        print('--------Edit Product in Cart--------')
        print('{}: {}{}'.format(product.name, info[0], info[1]))
        print('1. Edit quantity')
        print('2. Edit unit')
        print('3. Delete Product from Cart')
        print('9. Go back to previous page')

    @staticmethod
    def check_order(orders):
        print('--------Check Order--------')
        for i in range(len(orders)):
            print('{}. {}'.format(i + 1, orders))
        print('9. Go back to previous page')

    @staticmethod
    def owner_homepage():
        print('--------MFVS Owner--------')
        print('1. View Product')
        print('2. Change Password')
        print('3. Remove Customer Account')
        print('9. Exit')

    @staticmethod
    def view_product_detail_by_owner(product):
        print('--------View Product Detail--------')
        print(product)
        print('1. Edit Product')
        print('2. Back to Previous Page')
        print('9. Exit')

    @staticmethod
    def owner_edit_product():
        print('--------Edit Product--------')
        print('1. Edit Name')
        print('2. Edit Inventory')
        print('3. Edit Price')
        print('4. Set Current Date as Production Date')
        print('5. Edit Expiry Date')
        print('8. Go Back to Previous Page')
        print('9. Exit')

    @staticmethod
    def remove_account():
        print('--------Remove Account--------')

