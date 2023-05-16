# 병사를 열외시켜 내림차순 형태로 만들기
# 가장 병사의 수를 많이 남기고 싶을때 열외시킬 병사의 수는??

# 기본 아이디어: 가장 긴 증가하는 부분 수열
# LIS 알고리즘 수정 적용

# D[i] = array[i]
# 점화식: D[i] = max(D[i], D[j]+1) if array[j] < array[i] ( 0<= j < i)

n= int(input())
array = list(map(int,input().split()))
array.reverse()

dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))



