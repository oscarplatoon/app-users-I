# your User class goes here
import csv
import os

class User:

    def __init__(self, name, email_address, dl_number):
        self.name = name
        self.email_address = email_address
        self.dl_number = dl_number
    
    def __str__(self):
        return f'\n{self.name}\n-email: {self.email_address}\nDL number: {self.dl_number}\n'

    @classmethod
    def objects(cls):
        users = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/users.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                users.append(User(**dict(row)))

        return users
