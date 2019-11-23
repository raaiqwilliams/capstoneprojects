#Establishing nested for loops
#x range is up till 10 as we need 9 rows
#y range is up till (x+1) as we also need 9 columns

for x in range(1, 10):
    for y in range(1, x+1):
        print(x*y, end = ' ')   #printing product of x and y, along with a space to eliminate newline and instead print on same line
    print()                     #printing newline after each iteration of y to produce shape
