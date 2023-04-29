# 0~9 로만 이루어진 문자열 S사이에 *, + 를 넣어 가장 큰수 구하기
# 모든 연산은 왼쪽부터

n = input()
total = int(n[0])
for i in n[1:]:
    # if (int(i) ==0) or (total==0):
    if (int(i) <=1) or (total<=1):
        total += int(i)
    else :
        total *= int(i)
print(total)

# 1일때도 더하기가 유리한 점을 생각못함