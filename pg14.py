# List Comprehension
n = list(map(int,input("Enter numbers ").split()))
# (a) Display positive list of no.s from given list of numbers
p = [a for a in n if a>0]
print("positive numebrs:",p)
# (b) Generate a list with square of numbers from a given list 
s = [a**2 for a in n]
print("Squares:",s)
# (c) From a list of numbers by remeaning even no.s from a given list
odd = [a for a in n if a%2!=0]
print("Odd numbers: ",odd)
# (d) Display leap years from current year to a future year entered by user 
start = int(input("\n Enter current year:"))
end = int(input("\n Enter future year:"))
leap = [y for y in range(start,end+1)if(y%4==0) and (y%100!=0 or y%400 ==0)]
print("Leapyear: ",leap)