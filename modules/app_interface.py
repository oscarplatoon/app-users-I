from modules.application import Application


class AppInterface:
    def __init__(self, name):
        self.name = name
        self.application = Application(name)

    def run(self):
        print("Baseline user functionality Demo")

        while True:
            mode = input(self.print_menu())

            if mode == '1':
                print("Adding User...\n\n")
                self.add_user_prompts()
                print("Saved and added.")

            if mode == '2':
                for user in self.application.users:
                    print(user)

            if mode == '3':
                break

    def print_menu(self):
        return("Base Menu:\n1. Add a User \n2. Print Users\n3. Exit\n\nChoice: ")

    def add_user_prompts(self):
        user_data = {}
        user_data['name'] = input("Enter user name: ")
        user_data['email_address'] = input("Enter user email address: ")
        user_data['driver_license'] = input("Enter user driver license: ")
        user_data['valuable_pii'] = input("Enter user valuable PII: ")
        self.application.add_user(user_data)
