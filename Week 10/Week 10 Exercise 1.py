# Create the 'learning_python.txt' file with the provided content
file_path = 'c:/Users/Newbieility/OneDrive/Stanley College/Bachelor/ICT105 Programming Principles/Week 10/learning_python.txt'

# Content to be written in the file
content_to_write = [
    "In Python you can automate tasks using scripts.\n",
    "In Python you can perform data analysis with libraries like pandas.\n",
    "In Python you can build web applications with frameworks like Flask.\n",
    "In Python you can create machine learning models with libraries like scikit-learn.\n",
    "In Python you can manipulate images with libraries like PIL.\n"
]

# Write the content to the file
with open(file_path, 'w') as file:
    file.writelines(content_to_write)

# Reading and printing the entire content
with open(file_path, 'r') as file:
    content = file.read()

print("Printing the entire content:")
print(content)

# Reading lines into a list and printing line by line
with open(file_path, 'r') as file:
    lines = file.readlines()

print("Printing line by line:")
for line in lines:
    print(line.strip())
