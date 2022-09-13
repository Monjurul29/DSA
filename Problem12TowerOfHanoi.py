def towerOfHanoi(n, a, b, c):
    if n > 0:
        towerOfHanoi(n-1, a, c, b)
        print("Move disk", n, "from", a, "to", c)
        towerOfHanoi(n-1, b, a, c)


n = int(input("Enter the number of disk: "))
towerOfHanoi(n, 'A', 'B', 'C')