# 하루는 86,400초이므로 가능한 모든 시각의 경우를 세서 풀수 있는 문제
# 완전 탐색

h = int(input())

count = 0 
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count +=1

print(count)