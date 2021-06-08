class User():

    def __init__(self,name,email,drivers_license):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license



a = User('Andrew','andy80@yahoo.mail','iDriveGut')
b = User('Jen','jenjen@yahoo.mail','iDriveGut2')

print(f'Name: {a.name}\tEmail: {a.email}\tLicense: {a.drivers_license}')

print(f'Name: {b.name}\tEmail: {b.email}\tLicense: {b.drivers_license}')