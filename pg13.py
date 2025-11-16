# (a) Fibonacci of number

x, y = 0, 1
num = int(input("Enter the number: "))

if num <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci Series:")
    for i in range(num):
        print(x, end=" ")
        x, y = y, x + y

# (b) To find the sum of elements in  a list
s = list(map(int,input("Enter elements: ").split(",")))
print(s)
print("sum",sum(s))

# (c) Factorial of a number
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial of", n, "=", fact)
