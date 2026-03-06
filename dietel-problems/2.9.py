#using "ord" for the first time
#it's used to determine a string's integer value
#We are going sum up the integer value of each name to see who goes first
a= ord("T")
b = ord("o")
c = ord("m")
d = a+b+c

x = ord("J")
y = ord("i")
z = ord("m")
q= x+y+z

if d>q:
    print("Tom goes first")
elif d<q:
    print("Jim goes first")