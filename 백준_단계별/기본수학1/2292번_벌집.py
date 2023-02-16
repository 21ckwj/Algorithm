# 2 ~ 7 : 6
# 8 ~ 19 : 12
# 20 ~ 37 : 18

n = int(input())

cnt=1
n_sum = 1
while n > n_sum:
    n_sum += 6*cnt
    cnt = cnt+1
    
print(cnt)