import json

def store_favorite_number():
    favorite_number = input("Enter your favorite number: ")
    try:
        favorite_number = int(favorite_number)
    except ValueError:
        print("Please enter a valid number.")
        return

    with open('favorite_number.json', 'w') as f:
        json.dump(favorite_number, f)
    print("Your favorite number has been stored.")

store_favorite_number()
