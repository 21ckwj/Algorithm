# N가지 종류의 화폐
# 화폐의 개수를 최소한으로 이용해 가치의 합이 M이 되도록!
# M원을 만들기 위한 최소 화폐 개수 출력 프로그램

# n,m = map(int,input().split())
# coin_list = []
# for _ in range(n):
#     c = int(input())
#     coin_list.append(c)

# if m % c == 0 :
#     m 점화식 만들 생각부터 했어야지!!


# <풀이>
n,m = map(int,input().split())
array = []
for _ in range(n):
    array.append(int(input()))

# 한번 계산된 결과를 저장하기 위한 dp테이블 초기화
d = [10001] * (m+1)

# 다이나믹 프로그래밍
d[0] = 0
for i in range(n): # 코인개수
    for j in range(array[i], m+1): # 만드려는 가격
        if d[j-array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            # 원래방법보다 작은 것을 선택
            d[j] = min(d[j],d[j-array[i]]+1)
        
# 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])

