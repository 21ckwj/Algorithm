# 1 홀 1/1
# 2 짝 1/2 2/1
# 3 홀 3/1 2/2 1/3

x = int(input())
n=1
n_sum = 1
while x > n_sum:
    n_sum += n
    n +=1
    print(n)
    print(n_sum)
print(n)
# 짝수일때
if n%2 ==0:
    u = str(n-x+n_sum)+ '/' +str(x-n_sum) 
    print(u)
else:
    u = str(x-n_sum)+ '/' +str(n-x+n_sum)
    print(u)
    