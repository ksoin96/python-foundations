def maxoftwo(x,y):
   if x > y:
      return x
   return y
def maxofthree(x,y,z):
   larger = maxoftwo(x,y)

   largest= maxoftwo(larger,z)
   return largest

x = int(input("number 1: "))
y = int(input("number 2: "))
z = int(input("number 3: ") )
print(maxofthree(x,y,z))