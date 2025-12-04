# Password Validation Program

import re

pwd = input("Enter password: ")

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#]).{6,16}$'

if re.search(pattern, pwd):
    print("Valid Password")
else:
    print("Invalid Password")
