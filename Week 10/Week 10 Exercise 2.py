def add_two_numbers():
    try:
        # Prompting the user for two numbers
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        # Converting inputs to integers
        num1 = int(num1)
        num2 = int(num2)

        # Adding the numbers and printing the result
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}.")
        
    except ValueError:
        # Handling the case where the input is not a number
        print("One or both of the inputs are not valid numbers. Please enter numerical values only.")

# Running the function
add_two_numbers()
