# Find the sum of even-valued terms in a Fibonacci series

n = int(input("Enter limit: "))
a, b = 0, 1
total = 0

while a <= n:
    if a % 2 == 0:
        total += a
    a, b = b, a + b

print("Sum of even Fibonacci terms =", total)
