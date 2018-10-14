import re

class User:
    def __init__(self, new_id, username, password, email=None):
        self.id = new_id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return '{},{},{},{}'.format(self.id, self.username, self.password, self.email)

    def reset_password(self, new_password):
        if User.password_validation(new_password):
            self.password = new_password
            return True
        else:
            return False

    @staticmethod
    def email_validation(email):
        return True if '@' in email and ('.com' in email or '.edu' in email) else False

    @staticmethod
    def username_validation(username):
        return True if '@' in username and ('.com' in username or '.edu' in username) else False

    @staticmethod
    def password_validation(password):
        pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).*$"
        '''
        This pattern matches a string is longer than 8 characters and contains at least one:
            - Number
            - Lower case letter
            - Upper case letter
            - Special character
        '''
        return re.match(pattern, password)

    def change_password(self, new_password):
        if User.password_validation(new_password):
            self.password = new_password
            return True
        else:
            return False

    def change_username(self, new_username):
        if User.username_validation(new_username):
            self.username = new_username
            return True
        else:
            return False

    def change_email(self, new_email):
        if User.email_validation(new_email):
            self.email = new_email
            return True
        else:
            return False


class Customer(User):
    def __init__(self, new_id, username, password, email=None, first_name=None,
                 last_name=None, address=None, post_code=None, phone=None, status=0):
        super().__init__(new_id, username, password, email)
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.post_code = post_code
        self.phone = phone
        self.status = status  # 0 indicate that account is normal, not deleted by user

    def change_address(self, new_address):
        self.address = new_address

    def change_phone(self, new_phone):
        if str(new_phone).isnumeric():
            self.phone = int(new_phone)

    def __str__(self):
        return super().__str__() + '{},{},{},{},{},{}'\
            .format(self.first_name, self.last_name, self.address, self.post_code, self.phone, self.status)


class Owner(User):
    def __init__(self, new_id, username, password, email):
        super().__init__(new_id, username, password, email)

    @staticmethod
    def remove_customer(customer_id, customer_list):
        for customer in customer_list:
            if customer.id == customer_id:
                del customer_list[customer]
            break

    @staticmethod
    def modify_product_name(product, new_name):
        product.name = new_name

    @staticmethod
    def modify_product_date(product, new_date):
        product.expire_date = new_date
