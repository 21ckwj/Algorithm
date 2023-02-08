t = int(input()) # 테스트 횟수

for _ in range(t):
    a = input().split()
    r = int(a[0])
    string = a[1]
    for s in string:
        print(s * r,end='')