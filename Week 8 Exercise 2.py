def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

# Call the function three times with different numbers of arguments
make_sandwich('ham', 'cheese', 'lettuce', 'tomato')
make_sandwich('turkey', 'bacon')
make_sandwich('peanut butter', 'jelly', 'banana')
