from application import Application

test = Application("Test")


user_data = {}
user_data['name'] = input("Enter user name: ")
user_data['email_address'] = input("Enter user email address: ")
user_data['driver_license'] = input("Enter user driver license: ")
user_data['valuable_pii'] = input("Enter user valuable PII: ")
test.add_user(user_data)
test.save()
print(test.users)
