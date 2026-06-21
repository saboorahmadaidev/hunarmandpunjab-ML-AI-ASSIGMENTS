# Master Class\working_with_Formatted_user_profile_System.py
# Collects user info and writes a formatted profile to a file
name = input('Name: ')
age = input('Age: ')
city = input('City: ')
profile = f"Name: {name}\nAge: {age}\nCity: {city}\n"
fn = 'profiles.txt'
with open(fn, 'a') as f:
    f.write(profile + '\n')
print('Profile saved to', fn)
