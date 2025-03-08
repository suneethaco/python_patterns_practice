rows = 5
for i in range(rows):
    start_num = 7
    for j in range(rows-i-1):
        print(" ", end = "")
    for k in range(i+1):
        print(start_num, end = " ")
        start_num+=1
    print()