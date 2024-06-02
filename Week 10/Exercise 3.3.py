import json
import os

def get_user_info():
    # Ask the user for information
    username = input("Enter your username: ")
    age = input("Enter your age: ")
    location = input("Enter your location: ")
    return {"username": username, "age": age, "location": location}

def save_user_info(user_info):
    # Write the dictionary to a file
    with open("user_info.json", "w") as file:
        json.dump(user_info, file)

def load_user_info():
    # Read the dictionary back from the file
    with open("user_info.json", "r") as file:
        return json.load(file)

def verify_user(current_username):
    if not os.path.exists("user_info.json"):
        return False  # No user info file exists, so this is the first run
    else:
        user_info = load_user_info()
        last_username = user_info["username"]
        return current_username == last_username

def main():
    current_username = input("Enter your username: ")
    if verify_user(current_username):
        print("Welcome back!")
    else:
        print("You are not the last user of this program.")
        response = input("Are you a new user? (yes/no): ")
        if response.lower() == "yes":
            user_info = get_user_info()
        else:
            user_info = load_user_info()
    save_user_info(user_info)
    print("User Information:")
    for key, value in user_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
