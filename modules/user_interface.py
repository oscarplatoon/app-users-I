from modules.User import User

class UserInterface():
    def __init__(self):
        self.users = []
        self.run()

    def run(self):

        while True:
            input = self.menu()
            if input == 1:
                self.add_user()
            elif input == 2:
                self.delete_user()
            elif input == 3:
                self.view_users()
            elif input == 4:
                break
    
    def menu(self):
        return int(input("1. Add user\n2. Delete User\n3. View Users\n4. Quit\n> "))
    
    def add_user(self):
        name = input("Enter user name: ")
        email = input("Enter user email address: ")
        license = input("Enter user Driver's license: ")
        self.users.append(User(name, email, license))
        print(f"User {name} added.")
    
    def delete_user(self):
        license = input("Enter the driver's license number of the user to delete: ")
        for i, user in enumerate(self.users):
            if license == user.get_license():
                self.users.pop(i)
                print(f"User with license {license} deleted.")
                return
        
        print(f"Unable to find a user with license {license}.4")

    def view_users(self):
        for user in self.users:
            print(user)
    