# 정수 N이 입력되었을때 00시 00분 00초~ N시 59분 59초까지
# 모든 시각 중 3이 포함된 개수

n = int(input())

cnt = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time = str(h)+str(m)+str(s)
            # cnt += time.count("3") 모든 3의 개수가 아님!
            if '3' in time:
                cnt +=1
print(cnt)
