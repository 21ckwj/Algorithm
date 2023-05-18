# 모든 사람이 돈 인출하는 시간 최솟값

n = int(input())
time = list(map(int,input().split()))

time.sort()

total = 0
sum = 0
for t in time:
    sum += t
    total += sum

print(total)