import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "users.csv")





class User:
    all_posts = []
    
    def __init__(self, name, email_address, driver_license):
        self.name = name
        self.email_address = email_address
        self.driver_license = driver_license
        self.user_posts = []
    
    @classmethod
    def get_all_users(cls):
        with open(path) as users_file:
            users = csv.DictReader(users_file)
            users_list = []
            for user in users:
                new_user = User(user["name"], user["email_address"], user["driver_license"]) # creates brand new instance of user (User?) and simultaneously appending that to the users_list
                users_list.append(new_user)
        return users_list
    
    
    


























# import csv
# import os
# my_path = os.path.abspath(os.path.dirname(__file__))
# path = os.path.join(my_path, "users.csv")

# class User:
#     def __init__(self, name, email_address, drivers_license):
#         self.name = name
#         self.email_address = email_address
#         self.drivers_license = drivers_license
        
#     @classmethod
#     def get_all_users(cls):
#         with open(path) as users_file:
#             users = csv.DictReader(users_file)
#             users_list = []
#             for user in users:
#                 new_user = User(user["name"], user["email_address"], user["drivers_license"])
#                 users_list.append(new_user)
#         return users_list