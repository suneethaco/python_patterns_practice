n = 10
count = 0
for i in range(1, n+1):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if i+j+k == n:
                count+=1
print(count)
    