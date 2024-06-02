def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

# Call the function with the required information and two other name-value pairs
car_profile = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary to make sure all the information is stored correctly
print(car_profile)
