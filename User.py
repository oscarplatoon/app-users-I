# You have the next big thing on the interwebs.  But a thing isn't anything without users.  In your application, users can sign up with all kinds of valuable personal information like `name`, `email address`, `driver's licence number`, you name it.

# 1. Write a `User` class that can handle your growing application's needs.
# 2. Create a few users.

class User():
	def __init__(self, name, email_address, driver_license):
		self.name = name
		self.email_address = email_address
		self.driver_license = driver_license

	