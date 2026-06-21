# registration_system.py — simple registration saving to JSON
import json
fn = 'registered_users.json'

def load():
    try:
        with open(fn,'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save(users):
    with open(fn,'w') as f:
        json.dump(users, f, indent=2)

users = load()
name = input('Name: ')
email = input('Email: ')
password = input('Password (min 6): ')
if '@' not in email or len(password) < 6:
    print('Invalid input')
else:
    users.append({'name': name, 'email': email, 'password': password})
    save(users)
    print('Registered')
