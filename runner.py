from user import User

users = User()

while True:
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Users\n2. Add a User\n3. Delete User\n4. Quit\n")

    if mode == '1':
        self.list_users()
    elif mode == '2':
        self.add_user()
    elif mode == '3':
        self.delete_user()
    elif mode == '4':
        break

    def __init__(self):
         self.users = []


