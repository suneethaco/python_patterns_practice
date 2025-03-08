rows = int(input())
columns = int(input())
k = 7
for row in range(rows):
    for col in range(columns):
        print(k+col, end = " ")
    print()
    