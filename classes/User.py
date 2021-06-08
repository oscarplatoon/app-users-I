# your User class goes here
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, '..\classes\users.csv')

class User:

    def __init__(self, name, email, license):
        self.name = name
        self.email = email
        self.license = license

    @classmethod
    def get_all_users(cls):
        with open(path, 'r') as users_file:
            users = csv.DictReader(users_file)
            users_list = []
            for user in users:
                users_list.append(User(user['name'], user['email'], user['license']))
            return users_list

    # def add_user(self):
    #     return self.add_user

    # def add_email(self):
    #     return self.add_email

    # def add_license(self):
    #     return self.add_license

    # def get_name(self):
    #     return self.name

    # def get_email(self):
    #     return self.email

    # def get_license(self):
    #     return self.license