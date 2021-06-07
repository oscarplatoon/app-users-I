import csv
import os.path
from .user import User


class Application():
    def __init__(self, name):
        self.name = name
        self.users = User.objects()

    def add_user(self, user_data):
        self.users.append(User(**user_data))
        self.save()

    def save(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/users.csv")
        with open(path, 'w') as csvfile:
            user_csv = csv.writer(csvfile, delimiter=',')
            user_csv.writerow(['name', 'email_address', 'driver_license', 'valuable_pii'])
            for user in self.users:
                user_csv.writerow([user.name, user.email_address, user.driver_license, user.valuable_pii])