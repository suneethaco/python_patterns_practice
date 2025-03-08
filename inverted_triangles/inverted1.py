n = int(input())
for i in range(n):
    k = 1
    for j in range(n-i):
        print(k, end = " ")
        k += 1
    print()
        