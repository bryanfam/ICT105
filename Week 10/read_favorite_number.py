import json

def read_favorite_number():
    try:
        with open('favorite_number.json', 'r') as f:
            favorite_number = json.load(f)
        print(f"I know your favorite number! It’s {favorite_number}.")
    except FileNotFoundError:
        print("The favorite number file does not exist.")
    except json.JSONDecodeError:
        print("There was an error reading the favorite number.")

read_favorite_number()
