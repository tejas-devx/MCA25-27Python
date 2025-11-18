# Given a string of odd length > 7, return a new string made of the middle 3 characters

s = input("Enter a string of odd length > 7: ")

if len(s) > 7 and len(s) % 2 == 1:
    mid = len(s) // 2
    print("Middle 3 characters:", s[mid-1:mid+2])
else:
    print("Invalid input")
