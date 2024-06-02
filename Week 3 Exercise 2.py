guests = ["Alice", "Lucus", "Ryan"]

guests[1] = "David"  # Lucus can't make it, so inviting David instead
guests.insert(0, "Eve")
middle_index = len(guests) // 2  # Finding the middle index
guests.insert(middle_index, "Frank")  # Adding Frank to the middle of the list
guests.append("Grace")  # Adding Grace to the end of the list
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, we won't be able to invite you to dinner this time.")

for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

