# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
# 난이도 높지만 일반적으로 더 효율적
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1): # 인덱스 i부터 1까지 1씩 감소하며 반복
        # 앞의 숫자가 더 크다면 바꿔주기
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1],array[j]
        # 앞의 숫자가 더 작다면 그대로
        else: 
            break
print(array)
