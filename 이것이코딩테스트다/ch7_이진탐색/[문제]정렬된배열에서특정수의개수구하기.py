# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬
# 수열에서 x가 등장하는 횟수를 구하시오
# 단 시간복잡도 O(logN)으로 설계하지 않으면 시간초과판정

n, x = map(int,input().split())
array = list(map(int,input().split()))

# cnt = 0
# for i in array:
#     if i == x:
#         cnt +=1

# print(cnt)

# 일반적인 선형탐색의 경우 시간 초과

from bisect import bisect_left,bisect_right

def count_by_range(array,left_value,right_value):
    right_index = bisect_right(array,right_value)
    left_index = bisect_left(array,left_value)
    return right_index - left_index

count = count_by_range(array, x, x)
if count == 0:
    print(-1)
else:
    print(count)