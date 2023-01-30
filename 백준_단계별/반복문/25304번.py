# 총금액 X
# 물건종류수 N
# 물건가격, 물건개수 a,b

x = int(input())
n = int(input())

total = 0
for i in range(n):
    a, b = map(int,input().split())
    total += a*b
if total == x:
    print('Yes')
else:
    print('No')
