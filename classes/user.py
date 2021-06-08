import csv
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/info.csv")

class User:
    def __init__(self):
       pass
    
    @classmethod
    def objects(cls):
        users = []

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                users.append(User(**User(row)))
        return users

    user = []
    def add_to_csv(self, user_data):
        with open(path, 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames = ['role', 'first_name','last_name','email','password'])
            csv_writer.writerow(user_data)
            self.user.append(User(**user_data))
    

    def create_new_user(self):
        user_data = {'role': 'user'}

        user_data['first_name'] = input('please enter your first name: \n')
        user_data['last_name'] = input('please enter your last name: \n')
        user_data['email'] = input('Please enter your email adress: \n')
        user_data['password'] = input('Please create a secure password: \n')

        print(f"congradulations {user_data['first_name']} you have successfully created an account!")

        User.add_to_csv(self, user_data)

    
    

    