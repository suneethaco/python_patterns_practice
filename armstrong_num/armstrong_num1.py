n = 200
for i in range(1,n+1):
    str_num = str(i)
    len_str_num = len(str_num)
    sum = 0
    for j in str_num:
        num = int(j)
        res = num ** len_str_num
        sum += res
        if i == sum:
            print(i)
        
        
    
    