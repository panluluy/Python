row = 6
for i in range(1,row):
    for block in range(1,row-i):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end="")
    print()
