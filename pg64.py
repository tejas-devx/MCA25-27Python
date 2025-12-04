# Odd string length >7 → new string of middle three characters

s = input("Enter string: ")

if len(s) % 2 != 0 and len(s) > 7:
    mid = len(s) // 2
    print(s[mid-1 : mid+2])
else:
    print("String must be odd length and > 7")
