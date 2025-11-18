# Arrange characters so lowercase letters come first

s = input("Enter a string: ")

lower = "".join([ch for ch in s if ch.islower()])
upper = "".join([ch for ch in s if ch.isupper()])

print("Rearranged string:", lower + upper)
