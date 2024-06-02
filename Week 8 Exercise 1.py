def make_shirt(size, message):
    print(f"The size of the shirt is {size} and the message printed on it is '{message}'.")

# Call the function using positional arguments
make_shirt('Large', 'I love Python!')

# Call the function a second time using keyword arguments
make_shirt(size='Medium', message='Hello, World!')
