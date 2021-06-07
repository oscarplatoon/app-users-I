from classes.User import User
import time

class User_functions():

    def __init__(self):
        self.users = []
        self.runner()

    def runner(self):

        while True:
            mode = input("\nWhat would you like to do?\nOptions:\n1. Enter new user\n2. Show all Users\n5. Quit\n")

            if mode == '1':
                self.add_user()
            elif mode == '2':
                self.show_users()
            elif mode == '5':
                print("Exiting program")
                time.sleep(1)
                break  

    def add_user(self):
        name = input('Enter name:\n')
        email_address = input('Enter email address: \n')
        password = input('Enter password: \n')
        self.users.append(User(name, email_address, password))
        print(self.users)        
    
    def show_users(self):
        for user in self.users:
            print(user)