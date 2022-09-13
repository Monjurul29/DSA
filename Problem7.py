def matching(n, p):
    l1 = len(n)
    l2 = len(p)
    for i in range(l1 - l2 + 1):
        x = 0
        while x < l2:
            if n[i + x] != p[x]:
                break
            x = x + 1
        if x == l2:
           print("Pattern found at position : ", i)

n = input("Enter a string text: ")
p = input("Enter the pattern: ")
matching(n, p)