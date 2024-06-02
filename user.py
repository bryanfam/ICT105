# user.py

class User:
    def __init__(self, first_name, last_name, age, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username

    def describe_user(self):
        print(f"User profile for {self.username}:")
        print(f"  First Name: {self.first_name}")
        print(f"  Last Name: {self.last_name}")
        print(f"  Age: {self.age}")
        print(f"  Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.\n")
