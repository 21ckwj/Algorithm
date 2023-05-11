# 개미전사는 메뚜기 창고를 터는데 최소한 한칸 이상 떨어진
# 식량창고를 약탈해야함
# 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값?
# ex. 1 3 1 5 -> 8 최대

n = int(input())
array = list(map(int,input().split()))

# dp테이블
d = [0] * 100

# 다이나믹 프로그래밍
d[0] = array[0]
d[1] = max(array[0],array[1])

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])