import json

# Ask the user for information
username = input("Enter your username: ")
age = input("Enter your age: ")
location = input("Enter your location: ")

# Store the information in a dictionary
user_info = {
    "username": username,
    "age": age,
    "location": location
}

# Write the dictionary to a file
with open("user_info.json", "w") as file:
    json.dump(user_info, file)

# Read the dictionary back from the file
with open("user_info.json", "r") as file:
    loaded_user_info = json.load(file)

# Print a summary of the user information
print("User Information:")
for key, value in loaded_user_info.items():
    print(f"{key}: {value}")
