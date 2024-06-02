# Make a dictionary called cities
cities = {
    'Paris': {
        'country': 'France',
        'population': '2.1 million',
        'fact': 'Known as the "City of Light"'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '9.7 million',
        'fact': 'Has the busiest train station in the world'
    },
    'New York': {
        'country': 'USA',
        'population': '8.4 million',
        'fact': 'Home to the Statue of Liberty'
    }
}

# Print the name of each city and all of the information stored about it
for city, info in cities.items():
    print("City:", city)
    print("Country:", info['country'])
    print("Population:", info['population'])
    print("Fact:", info['fact'])
    print()
