import csv 
import os.path

class User():

    def __init__ (self, name=None, email=None, licence=None):
        self.users = []
        self.name= name
        self.email= email
        self.licence= licence

    def list_users (self):
        for user in self.users:
            print(user)
    
    def add_user (self, name, email, licence):
        self.users.append(User(name, email, licence))
        print (f"User {name} added")

    def delete_user(self):
        print("delete user")