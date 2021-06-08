from classes.User import User

class New_User_Interface:
    
    def __init__(self, name):#
        self.name = name
        self.user_account = []
        self.make_account()
        
    def make_account(self):
        welcome = print(f"Welcome {self.name}, please register your account\n")
        self.account_name = input('Please enter your full name: ')
        self.account_email = input('Please enter your email: ')
        self.user_account.append(User(self.account_name, self.account_email, user_name=None, user_password=None))
        print("Thanks for registering!")
        return self.make_username()

    def make_username(self):
         self.user_name = self.user_account.append([input('Please choose your user name: ')])
         self.user_password = self.user_account.append([input('Please choose your password: ')])
         self.user_account.append(User(self.account_name, self.account_email, self.user_name, self.user_password))
         self.confirm_account_info()

    def confirm_account_info(self):
        print(f"Please confirm your information\n")
        

            


   
