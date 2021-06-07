from user import User

class Interface:
    def run(self):
        while True:
            mode = input("1: Create new User!\n2: Login to existing account")

            if mode == '1':
                user_data = {'role': 'user'}

                user_data['first_name'] = input('please enter your first name: \n')
                user_data['last_name'] = input('please enter your last name: \n')
                user_data['email'] = input('Please enter your email adress: \n')
                user_data['password'] = input('Please create a secure password: \n')

                print(f"congradulations {user_data['first_name']} you have successfully created an account!")

                self.create_new_user(user_data)
