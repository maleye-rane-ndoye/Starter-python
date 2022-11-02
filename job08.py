#Rectangle
row = int(input("enter the number of rows:"))
col = int(input("enter the number of col:"))
for L in range(row):
    for H in range (col):
        if L==0 or L==(row-1):
            print("-",end="")
        elif H==0 or H==(col-1):
            print("|",end="")
        else:
            print(" ",end="")
    print()