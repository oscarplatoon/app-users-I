from User import User

class PremiumUser(User):
    def __init__(self, name, email_address, driver_license):
        super().__init__(name, email_address, driver_license)
        self.tier = "p"