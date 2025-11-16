# Pattern - pyramid
r = int(input("No of rows: "))
for i in range(1, r+1):
    print(" " * (r - i) + "*" * (2*i - 1))
