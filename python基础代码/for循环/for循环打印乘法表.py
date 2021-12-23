for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:<2}".format(i,j,i*j),end=" ")
    print()

print("{:*^60}".format("分割线"))

for i in range(1,10):
    for j in range(i,10):
        print("{}*{}={:<2}".format(i, j, i * j), end=" ")
    print()

print("{:*^60}".format("分割线"))

for i in range(9,0,-1):
    for block in range(9,i,-1):
        print(end="       ")
    for j in range(i,0,-1):
        print("{}*{}={:>2}".format(i, j, i * j), end=" ")
    print()

print("{:*^60}".format("分割线"))

for i in range(9,0,-1):
    for j in range(i,0,-1):
        print("{}*{}={:>2}".format(i, j, i * j), end=" ")
    for block in range(9,i,-1):
        print(end="       ")
    print()