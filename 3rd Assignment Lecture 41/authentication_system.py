# authentication_system.py — simple login against registered_users.json
import json
fn = 'registered_users.json'
try:
    with open(fn,'r') as f:
        users = json.load(f)
except FileNotFoundError:
    users = []

email = input('Email: ')
password = input('Password: ')
for u in users:
    if u.get('email') == email and u.get('password') == password:
        print('Login successful. Welcome', u.get('name'))
        break
else:
    print('Login failed')
