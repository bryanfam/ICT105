class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)
    
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number

# Creating an instance called restaurant
restaurant = Restaurant("The Great Feast", "Italian")

# Printing the number of customers served
print("Number of customers served:", restaurant.number_served)

# Changing the value and printing it again
restaurant.number_served = 50
print("Number of customers served (updated):", restaurant.number_served)

# Using set_number_served() method
restaurant.set_number_served(100)
print("Number of customers served (after set_number_served):", restaurant.number_served)

# Using increment_number_served() method
restaurant.increment_number_served(20)
print("Number of customers served (after increment_number_served):", restaurant.number_served)
