import csv
import os
from classes.User import User

class App:

    def __init__(self, name):
        self.name = name
        self.users = User.objects()

    def list_users(self):
        print('\n')
        for i, user in enumerate(self.users):
            print(f'{i + 1}. {user.name} {user.email_address}')

    def add_user(self, user_data):
        self.users.append(User(**user_data))
        self.save()



    def save(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/users.csv")

        with open(path, 'w') as csvfile:
            user_csv = csv.writer(csvfile, delimiter=',')
            user_csv.writerow(['name', 'email_address', 'dl_number'])
            for user in self.users:
                user_csv.writerow([user.name, user.email_address, user.dl_number])