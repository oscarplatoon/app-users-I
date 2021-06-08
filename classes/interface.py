from classes.User import User
class Interface:

    def menu(self):
        return('\n'
        'Menu\n'
        '1. Input Name:\n'
        '2. Input Email:\n'
        '3. Input License:\n'
        '4. Exit:\n')

    def run(self):
        while True:
            mode = input(self.menu())
            if mode == '1':
                self.add_name()
            elif mode == '2':
                self.add_email()
            elif mode == '3':
                self.add_license()
            elif mode == '4':
                break

