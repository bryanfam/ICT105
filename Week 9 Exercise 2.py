class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)
    
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")

# Creating an instance called restaurant
restaurant = Restaurant("The Great Feast", "Italian")

# Printing the attributes individually
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

# Calling both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Creating three different instances and calling describe_restaurant() for each instance
restaurant1 = Restaurant("Taste of India", "Indian")
restaurant2 = Restaurant("Sushi Palace", "Japanese")
restaurant3 = Restaurant("La Brasserie", "French")

print("\nDescription of each restaurant:")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
