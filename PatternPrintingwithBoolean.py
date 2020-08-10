#Pattern Printing

"""
input = Integer n
Boolean = True or False

True n = 5
*
**
***
****

False
****
***
**
*


"""

print('How many Row You want to Print')
one = int(input())
print('Type 1 or 0')
two = int(input())
new = bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print('*',end="")
        print()
elif new == False:
    for i in range(one,0-1):
        for j in range(i,i+1):
            print('*',end="")
        print()               

