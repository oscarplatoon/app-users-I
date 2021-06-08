import csv 
import os.path

class User():

    def __init__ (self, name=None, email=None, license=None):
        self.name= name
        self.email= email
        self.license= license

        # user_1 = User('vince, 'vzb@msn.com, R12345)

    @classmethod
    def get_all_users(cls):
       
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "user_info.csv")

        with open(path, 'r') as csvfile:
            users = csv.DictReader(csvfile) 
            users_list = []
            for user in users:
                print(user)
                # print(User(user['name'],user ['email'], user['license']))
                users_list.append(User(user['name'],user ['email'], user['license']))
            return users_list




    # def list_users (self):
    #     for user in self.users:
    #         print(user)
    
    # def add_user (self, name, email, licence):
    #     self.users.append(User(name, email, licence))
    #     print (f"User {name} added")

    # def delete_user(self):
    #     print("delete user")