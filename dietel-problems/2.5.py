#ypically 6 eggs fit in one box. Write a script to calculate the num-ber of boxes a farmer needs to store 28 eggs. The script will also determine how many eggsare placed in the last uncompleted box, and how many additional eggs are needed to fill this last box

x = int(input('How many eggs do you need to store?'))
y = x//6
z = x%6
if z == 0:
    total = y
else:
    total = y+1
print(f' You need {total} number of boxes')
print(f'There are {z} many apples  in the last box')
print(f'There are {6-z} many apples  needed to fill the last box')