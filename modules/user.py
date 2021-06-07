import csv
import os.path

class User():
    def __init__(self, name, email_address, driver_license, valuable_pii):
        self.name = name
        self.email_address = email_address
        self.driver_license = driver_license
        self.valuable_pii = valuable_pii

    def __str__(self):
        return(f"{self.name}, {self.driver_license}")

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

