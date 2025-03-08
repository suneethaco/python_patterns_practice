n = 7
count = 0
for i in range(1, n):
    for j in range(i+1, n+1):
        if(i+j == n):
            count+=1
print(count)