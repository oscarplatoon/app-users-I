# your User class goes here

class User:
    def __init__(self, account_name, account_email, user_name, user_password):
        self.name = account_name
        self.email = account_email
        self.user_name = user_name
        self.user_password = user_password

    def __str__(self):
        return f"Name - {self.name}\n Email - {self.email} \n User Name - {self.user_name} \n Password {self.user_password}"