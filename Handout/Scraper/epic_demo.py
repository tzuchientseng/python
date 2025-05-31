print("----------------------------------------", 'demo-login with json', "-"*40)
import json
import os
fn = os.path.join(os.path.dirname(__file__), 'login.json')

try:
    with open(fn) as fnObj:
        login = json.load(fnObj)
        print("Welcome back!")
except FileNotFoundError:
    login = input("Enter account: \n")
    with open(fn, 'w') as fnObj:
        json.dump(login, fnObj)
        print("Memorize your account!")

print("----------------------------------------", 'demo', "-"*40)
