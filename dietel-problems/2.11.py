a = int(input("Number of Seconds: "))
# find number of hours by dividing seconds by 3600
x= a//3600

# find number of minutes by using the remainder of seconds and true division with 60
y =(a%3600)//60

#think of remainder seconds after fiding hours and minutes
z = a%3600%60
print(f"{x}-{y}-{z}")