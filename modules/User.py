class User:
    def __init__(self, name, email, drivers_license):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license
    
    def __str__(self):
        return f"Name: {self.name}, Email Address: {self.email}, Driver's License: {self.drivers_license}"
    
    def get_license(self):
        return self.drivers_license