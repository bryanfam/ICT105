class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.login_attempts = 0  # Initialize login_attempts attribute
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# Creating an instance of User class
user1 = User("example_user", "user@example.com")

# Incrementing login attempts several times
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Printing the value of login_attempts to ensure it was incremented properly
print("Login attempts:", user1.login_attempts)

# Resetting login_attempts
user1.reset_login_attempts()

# Printing login_attempts again to ensure it was reset to 0
print("Login attempts after reset:", user1.login_attempts)
