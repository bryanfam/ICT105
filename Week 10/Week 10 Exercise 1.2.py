# File path
file_path = 'c:/Users/Newbieility/OneDrive/Stanley College/Bachelor/ICT105 Programming Principles/Week 10/learning_python.txt'

# Read lines from the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Replace 'Python' with 'C' and print each modified line
for line in lines:
    modified_line = line.replace('Python', 'C')
    print(modified_line.strip())
