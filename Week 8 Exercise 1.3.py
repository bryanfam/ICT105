def describe_city(city, country='Iceland'):
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city('Reykjavik')              # Uses the default country
describe_city('Akureyri')               # Uses the default country
describe_city('Paris', 'France')        # Specifies a different country
