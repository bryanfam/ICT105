current_users = ['admin', 'alice', 'bob', 'charlie', 'dave']
new_users = ['eve', 'frank', 'dave', 'grace', 'henry']

# Create a copy of current_users with lowercase usernames
current_users_lower = [user.lower() for user in current_users]

# Step 3b
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user}, this username is already taken. Please enter a new username.")
    else:
        print(f"Congratulations, {new_user}, the username is available!")