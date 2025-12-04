# Arrange characters so lowercase come first

s = input("Enter string: ")

lower = ''.join([c for c in s if c.islower()])
upper = ''.join([c for c in s if c.isupper()])

print(lower + upper)
