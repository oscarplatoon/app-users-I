from User import User
# from Post import Post

import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
user_path = os.path.join(my_path, "users.csv")
post_path = os.path.join(my_path, "posts.csv")

class Interface:
    def __init__(self):
        self.logged_in_user = None # user object
        self.loggedIn = False # initially set to false
        self.all_users = [] # instance method
        self.all_posts = []
        
    def run(self): # runs program
        input = self.start_menu() # see below for start menu
        # print("INPUT: ", input) see if needed to run program
        while True:
            if input == 1:
                self.add_user() # see add user def below
                break
            if input == 2: # add login def and subsequent def
                self.login()
                break
            if input == 3:
                print("Goodbye!")
                break
            
            
    def authenticated_menu(self):
        while self.loggedIn:
            print("""
            You're logged in!
            """)
            input = self.main_menu()
            if input == 1:
                self.view_users()
            elif input == 2:
                self.delete_user()
            elif input == 3:
                self.view_all_posts()
            elif input == 4:
                self.view_users_posts()
            elif input == 5:
                self.add_post()
            elif input == 6:
                self.logged_in_user = None
                self.loggedIn = False
                break
            
    def start_menu(self):
        return int(input("""
            1. Create user
            2. Login
            3. Exit
        """))
        
        
    def login(self):
        password = int(input("please enter your drivers license number: "))
        for user in User.get_all_users():
            if int(user.driver_license) == password:
                self.logged_in_user = user
                self.all_users = User.get_all_users() # assigning all users
                self.loggedIn = True
                self.all_posts = Post.get_all_posts() # create defs pertaining to posts
                return self.authenticated_menu()
        print("User not found.  try again. \n")
        return self.login
        
    def add_user(self):
        print("Enter new user information below")
        tier = input("Would you like a free or premium account? (f or p)")
        name = input("Enter user name: ")
        email = input("Enter user's email: ")
        drivers_license = int(input("Enter user's driver's license: "))
        all_users = Interface.get_all_users_from_db() # get info from Users 
        for user in all_users:
            if user.driver_license == drivers_license:
                print("A user already exists with that driver's license.  Try again")
                return self.add_user() # re-runs add_user method
        if tier[0].lower == "f":
            all_users.append(FreeUser(name, email, driver_license))
        elif tier[0].lower == "p":
            all_users.append(PremiumUser(name, email, driver_license))
           
            print("""
                New user created!
            """)
            self.save_users(all_users) # create save users below
            
    def save_users(self, all_users):
        with open(user_path, "w") as csvfile:
            user_csv = csv.writer(csvfile, delimiter = ",")
            user_csv.writerow(["name", "email_address", "driver_license", "tier"])
            for user in all_users:
                user_csv.writerow([user.name, user.email_address, user.driver_license, user.tier])
                
    def save_posts(self):
        with open(post_path, "w") as csvfile:
            post_csv = csv.writer(csvfile, delimiter = ",")
            post_csv.writerow(["user_id", "title", "body"])
            for post in self.all_posts:
                post_csv.writerow([post.user_id, post.title, post.body])
    
    def view_users(self):
        for user in self.all_users:
            print(user)
            
    def view_all_posts(self):
        for post in self.all_posts:
            print(post)
            
    def view_users_posts(self):
        for post in self.all_posts:
            if post.user_id == self.logged_in_user.driver_license:
                print(post)
                
    @classmethod
    def get_all_users_from_db(cls):
        with open(user_path) as users_file:
            users = csv.DictReader(users_file)
            users_list = []
            for user in users:
                if user["tier"] == "p":
                    premium_user = PremiumUser(user["name"], user["email_address"], user["driver_license"])
                    users_list.append(premium_user)
                else:
                    free_user = FreeUser(user["name"], user["email_address"], user["driver_license"])
                    users_list.append(free_user)
        return users_list
    
    




# User.get_all_users()





# print(User.get_all_users())