x1 = input("What's class 1? ")
x2 = int(input("What's the grade? "))

y1 = input("What's class 2? ")
y2 = int(input("What's the grade? "))

z1 = input("What's class 3? ")
z2 = int(input("What's the grade? "))

lc = x1
lowest = x2

if lowest > y2:
   lowest = y2 
   lc = y1
if lowest > z2:
   lowest = z2
   lc = z1
gc = z1
greatest = z2

if greatest < y2:
   greatest = y2 
   gc = y1

if greatest < x2:
   greatest = x2 
   gc = x1

print(lc,lowest)
print(gc,greatest)