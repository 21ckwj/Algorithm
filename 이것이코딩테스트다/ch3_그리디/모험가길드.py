# 모험가 N명
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹참여
# 여행을 떠날 수 있는 그룹의 최댓값?

n = int(input())
fear_list = list(map(int,input().split()))
fear_list.sort(reverse=True)

group = 0

# 잘 모르겠음