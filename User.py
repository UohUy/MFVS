class User:
    def __init__(self, new_id, username, password, email):
        self.id = new_id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return self.username

    def reset_password(self, new_password):
        if User.password_validation(new_password):
            self.password = new_password

    @staticmethod
    def username_validation(username):
        return True if '@' in username and ('.com' in username or '.edu' in username) else False

    @staticmethod
    def password_validation(password):
        import re
        # pattern = re.compile(r'(\d+)([a-z]+)([A-Z]+)(\W+)(\S{' + str(len(password)) + '})')
        pattern = re.compile(r'(\d+)')
        return re.findall(pattern, password)


class Customer(User):
    def __init__(self, new_id, username, password, email):
        super().__init__(new_id, username, password, email)
        self.first_name = None
        self.last_name = None
        self.address = None
        self.phone = None


class Owner(User):
    def __init__(self, new_id, username, password, email):
        super().__init__(new_id, username, password, email)

    def remove_customer(self, customer_id):
        pass


