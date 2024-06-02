# Step 1: Create and write to cats.txt and dogs.txt
with open('cats.txt', 'w') as file:
    file.write("Whiskers\nPaws\nFluffy\n")

with open('dogs.txt', 'w') as file:
    file.write("Rover\nSpot\nFido\n")

# Step 2: Read the files and handle FileNotFoundError
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
            print(f"Contents of {file_name}:\n{contents}")
    except FileNotFoundError:
        # To print a friendly message if a file is missing, uncomment the line below
        # print(f"Sorry, the file {file_name} was not found.")
        # To fail silently if a file is missing, just pass
        pass

# Read the files
read_file('cats.txt')
read_file('dogs.txt')
