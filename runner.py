from classes.app import App

app = App("Marc's App")
mode = ''


while mode != '5':
    mode = input("\nWhat would you like to do?\nOptions:\n1. Add a User\n2. List Users\n5. Quit\n")
    if mode == '1':
        user_data = {}
        user_data['name'] = input("Enter your name: ")
        user_data['email_address'] = input("Enter your email address: ")
        user_data['dl_number'] = input("Enter your driver's license number: ")
        app.add_user(user_data)

    elif mode == '2':
        app.list_users()
    elif mode == '5':
        break
    else:
        pass