# N이 1이 될때까지 두과정 반복
# N 에서 -1, n 나누기 k
# 입력 N, k

n,k = map(int,input().split())
cnt = 0
while n>1:
    if n%k==0:
        n = n//k
    else:
        n -= 1
    print(n)
    cnt +=1
print(cnt)
