from classes.user import User

class Interface:
    
    def run(self):
        while True:
            mode = input("\n1: Create new User!\n2: Login to existing account\n3: Quit application\n")

            if mode == '1':
              User.create_new_user(self)
            elif mode == '3':
                break
