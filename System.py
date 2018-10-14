import csv
import datetime
import hashlib
import uuid

from Cart import Cart
from Order import Order
from Product import Fruit, Vegetable
from UI import UI
from User import Customer, Owner


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
        self._load_customer_data()
        self._load_owner_data()
        self._load_product_data()

    def _load_customer_data(self):
        # load customer list
        with open("user_file.csv", "r") as user_file:
            # read csv file by line
            csv_lines = csv.reader(user_file)
            # store the whole user list into attribute "customers"
            for line in csv_lines:
                customer = Customer(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
                self.customers.append(customer)
        user_file.close()

    def _load_owner_data(self):
        # load owner list
        with open("owner_file.csv", "r") as owner_file:
            # read csv file by line
            csv_lines = csv.reader(owner_file)
            # store the whole user list into attribute "owners'
            for line in csv_lines:
                owner = Owner(line[0], line[1], line[2], line[3])
                self.owners.append(owner)
        owner_file.close()

    def _load_product_data(self):
        # load owner list
        with open("product_file.csv", "r") as product_file:
            # read csv file by line
            csv_lines = csv.reader(product_file)
            # store the whole user list into attribute "owners'
            for line in csv_lines:
                if line[3] == 'fruit':
                    product = Fruit(line[0], line[1], [line[2]], line[4], float(line[5]), int(line[6]), line[7],
                                    line[8], line[9])
                else:
                    product = Vegetable(line[0], line[1], [line[2]], line[4], float(line[5]), int(line[6]), line[7],
                                        line[8], line[9])
                self.products.append(product)
        product_file.close()

    def save_data(self):
        self._save_customer_data()
        self._save_owner_data()
        self._save_customer_data()

    def _save_owner_data(self):
        owner_file = open('owner_file.csv', 'w')
        for o in self.owners:
            owner_file.write(o.__str__)
        owner_file.close()

    def _save_customer_data(self):
        customer_file = open('user_file.csv', 'w')
        for c in self.customers:
            customer_file.write(c.__str__)
        customer_file.close()

    def _save_product_data(self):
        product_file = open('product_file.csv', 'w')
        for p in self.products:
            product_file.write(p.__str__)
        product_file.close()

    def start_up(self):
        while True:
            UI.homepage()
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
                self.wrong_selection()

    def customer_login(self):
        usn = input('Username: ')
        psd = input('Password: ')
        login = False
        for customer in self.customers:
            if usn == customer.username and md5_encrypt(psd) == customer.password and customer.status == 0:
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
            if usn == owner.username and md5_encrypt(psd) == owner.password:
                self.login_user = owner
                login = True
        if login:
            self.owner_home_page()
        else:
            print("Username and password are not matched")

    def create_account(self):
        usn = input('Please input a username: ')
        psd1 = input('Please input a password: ')
        psd2 = input('Please input password again: ')
        if psd1 != psd2:
            print("Password don't match")
        elif usn in [c.username for c in self.customers]:
            print('Username is occupied')
        elif not Customer.password_validation(psd1):
            UI.password_valid_information()
        else:
            first_name = input("Please input your first name: ")
            last_name = input('Please input your last name: ')
            email = input('Please input your email: ')
            address = input('Please input your address: ')
            post_code = input('Please input your post code: ')
            phone = input('Please input your phone number: ')
            customer = Customer(generate_id(), usn, md5_encrypt(psd1), email, first_name, last_name, address, post_code,
                                phone)
            self.customers.append(customer)

    def customer_delete_account(self):
        while True:
            x = input('Delete account? y/n')
            if x == 'n':
                break
            elif x == 'y':
                psw = input('Please input your password')
                if md5_encrypt(psw) == self.login_user.password:
                    self.login_user.status = 1
                else:
                    print('Password incorrect')
                break
            else:
                print("Please enter 'y' or 'n' ")

    def customer_home_page(self):
        while True:
            UI.customer_homepage()
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
                self.check_cart()
            elif x == '5':
                self.check_order()
            elif x == '6':
                self.modify_account()
            elif x == '7':
                self.customer_delete_account()
                break

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
                index = int((index - 1) % (len(products) / 5))
            elif n == '8':
                index = int((index + 1) % (len(products) / 5))
            elif '1' <= n <= '5' and int(n) <= len(parse_product[index]):
                self.view_product_detail(parse_product[index][int(n)])
            else:
                self.wrong_selection()

    def view_product_detail(self, product):
        if self.login_user in self.customers:
            self._view_product_detail_by_customer(product)
        else:
            self._view_product_detail_by_owner(product)

    def _view_product_detail_by_customer(self, product):
        UI.view_product_detail_by_customer(product)
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
                self.wrong_selection()

    def _view_product_detail_by_owner(self, product):
        UI.view_product_detail_by_owner(product)
        while True:
            n = input('Please input your option: ')
            if n == '9':
                self.exit()
            elif n == '2':
                break
            elif n == '1':
                self.owner_edit_product(product)
                UI.view_product_detail_by_owner(product)
            else:
                self.wrong_selection()

    def add_to_cart(self, product):
        unit_type = product.unit
        # get unit
        while True:
            for i in range(len(unit_type)):
                print('{}. {}'.format(i + 1, unit_type[i]))
            unit_index = input("Please input product's unit")
            if '0' <= unit_index < str(len(unit_type)):
                unit = unit_type[int(unit_index) - 1]
                break
            else:
                self.wrong_selection()
        # get quantity
        while True:
            qty = input("Please input product's quantity")
            if not qty.isnumeric():
                print('Please input an integer number')
            else:
                qty = int(qty)
                break
        # TODO Need to make sure quantity multiple unit won't greater than stock
        self.cart[product] = (qty, unit)

    def sort_product(self):
        UI.sort_product()
        while True:
            n = input('Please input an option: ')
            if n == '1':
                self.products.sort(key=name_key)
                break
            elif n == '2':
                self.products.sort(key=name_key, reverse=True)
                break
            elif n == '3':
                self.products.sort(key=price_key)
                break
            elif n == '4':
                self.products.sort(key=price_key, reverse=True)
                break
            else:
                self.wrong_selection()

    def modify_account(self):
        UI.modify_customer_account()
        while True:
            n = input('Please input an option: ')
            if n == '1':
                self.change_account_username()
                break
            elif n == '2':
                self.change_account_password()
                break
            elif n == '3':
                break
            elif n == '9':
                self.exit()
            else:
                self.wrong_selection()

    def change_account_username(self):
        UI.edit_username()
        new_usr = input('Please input a new username: ')
        if Customer.username_validation(new_usr):
            self.login_user.username = new_usr
            print('New username is: ', new_usr)
        else:
            print('Username is invalid')

    def change_account_password(self):
        UI.edit_password()
        old_psd = input('Please input old password: ')
        new_psd_1 = input('Please input new password: ')
        new_psd_2 = input('Please input new password again: ')
        if new_psd_1 != new_psd_2:
            print('New passwords are not matched')
        elif md5_encrypt(old_psd) == self.login_user.password:
            print('New password is same with old password')
        elif not Customer.password_validation(new_psd_1):
            UI.password_valid_information()
        else:
            self.login_user.password = md5_encrypt(new_psd_1)

    def check_cart(self):
        UI.check_cart(self.cart)
        while True:
            n = input('Please input your option: ')
            if n == '9':
                break
            elif n == '6':
                self.cart.clear()
                print('Cart is successfully cleared')
                break
            elif n == '7':
                self.edit_cart()
                break
            elif n == '8':
                self.generate_order()
                break
            else:
                self.wrong_selection()

    def edit_cart(self):
        UI.edit_cart(self.cart)
        while True:
            n = input('Please input your option: ')
            if n == '9':
                break
            elif '1' <= n <= str(len(self.cart)):
                product = self.cart.item_list.keys()[int(n) - 1]
                info = self.cart.item_list.values()[int(n) - 1]
                self.edit_product_in_cart(product, info)
                break
            else:
                self.wrong_selection()

    def edit_product_in_cart(self, product, info):
        UI.edit_product_in_cart(product, info)
        while True:
            n = input('Please input your option: ')
            if n == '9':
                break
            elif n == '1':
                self._edit_product_quantity_in_cart(product, info)
                break
            elif n == '2':
                self._edit_product_unit_in_cart(product, info)
                break
            elif n == '3':
                del self.cart[product]
                break
            else:
                self.wrong_selection()

    def _edit_product_quantity_in_cart(self, product, info):
        while True:
            qty = input('Please input a new qty')
            if qty.isnumeric() and 0 < int(qty) <= int(product.inventory):
                info[0] = int(qty)
                break
            else:
                print('Input quantity is invalid')
                continue

    def _edit_product_unit_in_cart(self, product, info):
        while True:
            unit = input('Please input a unit')
            if unit in product.unit:
                info[1] = unit
                break
            else:
                print('Input unit is invalid, please input a unit within {}'.format(product.unit))

    def generate_order(self):
        order = Order(generate_id(), self.cart.item_list, self.login_user.id, current_date(), self.cart.total_due)
        self.orders.append(order)
        self.check_out(order)

    def check_order(self):
        order_belongs_current_customer = self._check_order()
        UI.check_order(order_belongs_current_customer)
        while True:
            n = input('Please select a order: ')
            if n == '9':
                break
            elif n.isnumeric():
                if 0 < int(n) <= len(order_belongs_current_customer):
                    self.check_out(order_belongs_current_customer[int(n) - 1])
                break
            else:
                self.wrong_selection()

    def _check_order(self):
        return [o for o in self.orders if o.customer_id == self.login_user.id]

    def check_out(self, order):
        print(order)
        if order.payment_status == 0:
            while True:
                n = input('Do you want to check out now? y/n')
                if n == 'y':
                    order.payment_status = 1
                    for key, value in order.item:
                        key.inventory -= value[0]
                    print('Order is successfully checked out')
                    break
                elif n == 'n':
                    break
                else:
                    print("Please input 'y' or 'n'")
        else:
            while True:
                n = input('9. Go back to previous page')
                if n == '9':
                    break
                else:
                    self.wrong_selection()

    def owner_home_page(self):
        UI.owner_homepage()
        while True:
            n = input('Please input your selection')
            if n == '9':
                self.exit()
            elif n == '1':
                self.view_product()
            elif n == '2':
                self.change_account_password()
            elif n == '3':
                self.remove_customer_account()
            else:
                self.wrong_selection()

    def owner_edit_product(self, product):
        UI.owner_edit_product()
        while True:
            n = input('Please input your selection')
            if n == '9':
                self.exit()
            elif n == '8':
                break
            elif n == '1':
                self.owner_edit_product_name(product)
            elif n == '2':
                self.owner_edit_product_Inventory(product)
            elif n == '3':
                self.owner_edit_product_price(product)
            elif n == '4':
                self.owner_set_product_production_date(product)
            elif n == '5':
                self.owner_edit_product_expiry_date(product)
            else:
                self.wrong_selection()
                continue
            break

    def owner_edit_product_name(self, product):
        print('Old product name:', product.name)
        name = input('Please input a new name: ')
        product.name = name
        print('Name is successfully changed')

    def owner_edit_product_price(self, product):
        print('Old product price:', product.price)
        price = input('Please input a new price: ')
        if Product.price_validation(price):
            product.price = float(price)
        else:
            print('Wrong price entered')

    def owner_edit_product_Inventory(self, product):
        print('Old product inventory:', product.inventory)
        invt = input('Please input total inventory:')
        if invt.isnumeric():
            product.inventory = int(invt)
        else:
            print('Wrong inventory entered')

    def owner_edit_product_expiry_date(self, product):
        print('Old product expiry date is:', product.expiry_day)
        date = input('Please input new expiry date (in dd/mm/yyyy format): ')
        if validate_date(date):
            product.expiry_day = date
        else:
            print('Wrong date')

    def owner_set_product_production_date(self, product):
        product.production_date = current_date()
        print('Production date changed to:', current_date())

    def remove_customer_account(self):
        UI.remove_account()
        account = None
        username = input('Please input username you want to remove: ')
        for c in self.customers:
            if c.username == username:
                account = c
            break
        if account is not None:
            psw = input('Please enter your password to confirm remove this account: ')
            if md5_encrypt(psw) == self.login_user.password:
                self.customers.remove(account)
                print('Account "{}" is removed'.format(username))
            else:
                print('Wrong password')
        else:
            print('Can not find this account:', username)

    def wrong_selection(self):
        print('Please input a correct option\n')

    def exit(self):
        print('Thanks for using MFVS')
        self.save_data()
        exit(0)


def name_key(product):
    return product.name


def price_key(product):
    return product.price


def generate_id():
    return uuid.uuid4()


def md5_encrypt(string):
    m = hashlib.md5()
    m.update(str.encode(string))
    md5value = m.hexdigest()
    return md5value


def current_date():
    today = datetime.date.today()
    return today.strftime('%d/%m/%Y')


def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
    except ValueError:
        return False
