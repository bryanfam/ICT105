def build_profile(first_name, last_name, **user_info):
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Build a profile for yourself
my_profile = build_profile('Bryan', 'Fam', age=27, occupation='Software Developer', location='Australia')

print(my_profile)
