#  “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 
# 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”

#  모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때,
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
# k층에 n호에는 몇 명이 살고 있는지 출력하라

t = int(input())
for _ in range(t):
    floor = int(input())
    num = int(input())

    # 0층~ k-1층
    total = 0
    # 그러면 k-1층은 1호 1명,2호 1+2명,...b호 1+2...+b
    sum = 0
    for j in range(1,n+1):
        sum += j

    total += sum 
    print(total)