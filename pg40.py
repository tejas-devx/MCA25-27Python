# Check whether a given positive integer is power of 2. Raise exception for negative input

def is_power_of_two(n):
    if n < 0:
        raise ValueError("Negative input is not allowed")

    return n > 0 and (n & (n - 1)) == 0



try:
    num = int(input("Enter a number: "))
    if is_power_of_two(num):
        print("Power of 2")
    else:
        print("Not a power of 2")
except ValueError as e:
    print(e)
