x = int(input("How many marbles you want to distribute? "))
y= int(input("How many friends do you have? "))

z = x//y
p = x-(y*z)
if p != 0:
	print("No, you can't evenly distribute them")
else:
	print("Yes, you can evenly distribute them")