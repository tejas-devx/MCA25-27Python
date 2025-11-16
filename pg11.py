# Wap to print factors of a given number.
n = int(input("Number:"))
fact = 1
for i in range(1,n+1):
    fact*= i
print("factorial of",n,"=",fact)