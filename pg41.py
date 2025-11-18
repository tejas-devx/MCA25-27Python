# Find the sum of even-valued terms in a Fibonacci series

limit = int(input("Enter the upper limit for the Fibonacci series: "))

a, b = 0, 1
total = 0

while a <= limit:
    if a % 2 == 0:
        total += a
    a, b = b, a + b

print("Sum of even-valued Fibonacci terms =", total)
