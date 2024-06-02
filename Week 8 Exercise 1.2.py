def make_shirt(size='Large', message='I love Python'):
    print(f"The size of the shirt is {size} and the message printed on it is '{message}'.")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size='Medium')

# Make a shirt of any size with a different message
make_shirt(size='Small', message='Yolo')
