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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print("- " + flavor)

# Creating an instance of IceCreamStand
ice_cream_stand = IceCreamStand("Cool Cones", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry", "Mint"])

# Calling the method to display flavors
ice_cream_stand.display_flavors()
