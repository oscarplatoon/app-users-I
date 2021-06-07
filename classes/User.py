# your User class goes here


class User():
    
    def __init__(self, name):#
        self.name = name
        self.user_account = []

    def run(self):
        self.account_made = None
        run_account = self.run()
        self.make_account()
        if self.account_made == None:
            print('Please try again')
            while self.account_made == True:
                print('tested')

    def make_account(self):
        print(f'Welcome to the App Store!\n')
        enter_info = self.user_account.append(input("Please enter your full name to register an account: "))
        email_info = self.user_account.append(input("Please enter your email: "))
        self.account_made == True
        return run_account

    def pick_user_name(self):
        self.user_name = self.user_account.append(input('Please choose a user name: '))
        self.user_password = self.user_account.append(input('Please choose a user name: '))
