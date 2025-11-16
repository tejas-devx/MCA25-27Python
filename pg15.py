#Wap to add 'ing' at the end of the string.If already ends with 'ing,then add 'ily'

s = input("Enter a string: ")

if len(s) >= 3:
    if s.endswith("ing"):
        s += "ly"
    else:
        s += "ing"

print("New string:", s)
