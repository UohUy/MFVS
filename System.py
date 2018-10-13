import uuid

from Cart import Cart
from UI import UI
from User import Customer


class System:
    def __init__(self):
        self.products = []
        self.customers = []
        self.owners = []
        self.orders = []
        self.login_user = None
        self.load_data()
        self.cart = Cart()

    def load_data(self):
        pass

    def save_data(self):
        pass

    def start_up(self):
        UI.homepage()
        while True:
            x = input('Please input your selection: ')
            if x == '9':
                self.exit()
            elif x == '1':
                self.customer_login()
            elif x == '2':
                self.owner_login()
            elif x == '3':
                self.create_account()
            else:
                print('Please input correct option')

    def customer_login(self):
        usn = input('Username: ')
        psd = input('Password: ')
        login = False
        for customer in self.customers:
            if usn == customer.username and psd == customer.password:
                self.login_user = customer
                print('Welcome, {}'.format(customer.first_name))
                login = True
        if login:
            self.customer_home_page()
        else:
            print("Username and password are not matched")

    def owner_login(self):
        usn = input('Username: ')
        psd = input('Password: ')
        login = False
        for owner in self.owners:
            if usn == owner.username and psd == owner.password:
                self.login_user = owner
                login = True
        if login:
            self.owner_home_page()
        else:
            print("Username and password are not matched")

    def create_account(self):
        usn = input('Please input a username: ')
        psd1 = input('Please input a password: ')
        psd2 = input('Please input your again: ')
        if psd1 == psd2:
            print("Password don't match")
        elif usn in [u.username for u in self.customers]:
            print('Username is occupied')
        elif not Customer.password_validation(psd1):
            print('Password needs contain at least:'
                  '\n\t- one upper case letter;'
                  '\n\t- one lower case letter'
                  '\n\t- one number'
                  '\n\t- one special character'
                  '\nAnd length has to longer than 8 characters')
        else:
            first_name = input("Please input your first name: ")
            last_name = input('Please input your last name: ')
            email = input('Please input your email: ')
            address = input('Please input your address: ')
            post_code = input('Please input your post code: ')
            phone = input('Please input your phone number: ')
            customer = Customer(uuid.uuid1(), usn, psd1, email, first_name, last_name, address, post_code, phone)
            self.customers.append(customer)

    def customer_delete_account(self):
        while True:
            x = input('Delete account? y/n')
            if x == 'n':
                break
            elif x == 'y':
                psw = input('Please input your password')
                if psw == self.login_user.password:
                    del self.customers[self.login_user]
                else:
                    print('Password incorrect')
            else:
                print("Please enter 'y' or 'n' ")

    def customer_home_page(self):
        UI.customer_homepage()
        while True:
            x = input('Please input your selection: ')
            if x == '9':
                self.exit()
            elif x == '1':
                self.view_product()
            elif x == '2':
                self.search_product()
            elif x == '3':
                self.sort_product()
            elif x == '4':
                self.modify_account()
            elif x == '5':
                self.check_out()
            elif x == '6':
                self.customer_delete_account()

    def search_product(self):
        name = input('Please input product name: ')
        result = None
        for p in self.products:
            if p.name == name:
                result = p
        if result is None:
            print("No matched result")
        else:
            self.view_product([result])

    def view_product(self, products=None):
        if products is None:
            products = self.products
        parse_product = [products[i:i + 5] for i in range(0, len(self.products), 5)]
        index = 0
        while True:
            UI.view_product(parse_product[index])
            n = input('Please input your option: ')
            if n == '9':
                # Here is go back to previous page, not exit this system
                break
            elif n == '7':
                index = (index - 1) % len(products)
            elif n == '8':
                index = (index + 1) % len(products)
            elif '1' <= n <= '5' and int(n) <= len(parse_product[index]):
                self.view_product_detail(parse_product[index][int(n)])
            else:
                print('Please input a correct option')

    def view_product_detail(self, product):
        UI.view_product_detail(product)
        while True:
            n = input('Please input your option: ')
            if n == '9':
                self.exit()
            elif n == '1':
                self.add_to_cart(product)
                break
            elif n == '2':
                pass
            else:
                print('Please input a correct option')

    def add_to_cart(self, product):
        unit_type = product.unit
        # get unit
        while True:
            for i in range(len(unit_type)):
                print('{}. {}'.format(i + 1, unit_type[i]))
            unit = input("Please input product's unit")
            if '0' <= unit < str(len(unit_type)):
                unit = unit_type[unit]
                break
            else:
                print('Please input correct option')
        # get quantity
        while True:
            qty = input("Please input product's quantity")
            if not qty.isnumeric():
                print('Please input number')
            elif int(qty).__class__ is not int:
                print('Please input integer number')
            else:
                qty = int(qty)
                break
        # TODO Need to make sure quantity multiple unit won't greater than stock
        self.cart[product] = (unit, qty)

    def sort_product(self):
        UI.sort_product()
        while True:
            n = input('Please input an option: ')
            if n == '1':
                self.products.sort(key=name_key)
            elif n == '2':
                self.products.sort(key=name_key, reverse=True)
            elif n == '3':
                self.products.sort(key=price_key)
            elif n == '4':
                self.products.sort(key=price_key, reverse=True)

    def modify_account(self):
        pass

    def check_out(self):
        pass

    def owner_home_page(self):
        pass

    def exit(self):
        print('Thanks for using MFVS')
        self.save_data()
        exit(0)


def name_key(product):
    return product.name


def price_key(product):
    return product.price
