# main_program.py

from user import User

# Creating instances of the User class
user1 = User('John', 'Doe', 28, 'john.doe@hotmail.com', 'johndoe')
user2 = User('Jane', 'Smith', 34, 'jane.smith@hotmail.com', 'janesmith')
user3 = User('Alice', 'Johnson', 45, 'alice.johnson@hotmail.com', 'alicej')

# Calling methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
