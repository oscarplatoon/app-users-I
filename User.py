class User:
    def __init__(self,first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        
    def create_new_user(self):
        user_info = {'role': 'user'}

        user_info['first_name'] = input('please enter your first name.')
        user_info['last_name'] = input('please enter your last name.')
        user_info['email'] = input('Please enter your email adress.')
        user_info['password'] = input('Please create a secured password! your almost done!')

        print(f"congradulations {user_info['first_name']} you have successfully created an account!")