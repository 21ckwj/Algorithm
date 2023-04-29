# 시간복잡도 고려
# 나누는 연산 최소화: 나눌 수 있을때만 나누기 실행
n, k = map(int,input().split())

result = 0 

while True:
    # n이 k로 나누어 떨어지는 수가 될때까지 빼기
    target = (n//k) * k
    result += (n-target)
    n= target

    # N이 k보다 작을때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n <k:
        break
    # K로 나누기
    result += 1
    n //=k

result += (n-1)
print(result)