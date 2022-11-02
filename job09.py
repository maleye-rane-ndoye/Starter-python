#Triangle
n =int(input("enter the number of row:"))
for row in range (1,n+1):
    for col in range(1,2*n):
        if row==n:
            print("-",end="")
        elif row+col==n+1:
            print("/",end="")
        elif col-row==n-1:
            print('\\',end="")
        else:
            print(end=" ")
    print()