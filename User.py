import csv
class User:

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.data_dict = {}
        self.data_dict['username'] = self.username
        self.data_dict['password'] = self.password
        self.data_dict['email'] = self.email

    
    def save(self):
        with open(f'{self.username}.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['username', 'password', 'email'])
            writer.writeheader()
            writer.writerow(self.data_dict)
            

jake = User('jakewhite5', 'xx', 'jakewhite5@yahoo.com')

jake.save()