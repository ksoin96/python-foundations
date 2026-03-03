#minimum—the smallest value in a collection of value
#maximum—the largest value in a collection of values
#Range—the range of values from the minimum to the maximum
#Count—the number of values in a collection
#sum—the total of the values in a collection

#Here's a script below determining the lowest value of three.

x = int(input("Please enter number: "))
y = int(input("Please enter number: "))
z = int(input("Please enter number: "))
a = x
if a > y:
    a = y
if a > z:
    a = z

print(f"The lowest number is {a}")

#more functional style programming would be using the max and min functions below

print(max(1,8,9))

print(min(1,8,9))