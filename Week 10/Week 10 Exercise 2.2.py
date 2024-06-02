def add_two_numbers():
    while True:
        try:
            # Prompting the user for two numbers
            num1 = input("Enter the first number (or 'q' to quit): ")
            if num1.lower() == 'q':
                break
            num2 = input("Enter the second number (or 'q' to quit): ")
            if num2.lower() == 'q':
                break

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
