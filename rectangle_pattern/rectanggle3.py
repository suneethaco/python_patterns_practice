m = 5
n = 8
k = m * n
for i in range(m):
    for j in range(n):
        print(k, end = " ")
        k -= 1
    print()