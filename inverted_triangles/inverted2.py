n = int(input())
s= n * (n+1)//2
for i in range(n):
    for j in range(i):
        print(" ", end = " ")
    for k in range(n-i):
        print(s, end = " ")
        s-=1
    print()