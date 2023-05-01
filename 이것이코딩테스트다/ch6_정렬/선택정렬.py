# 처리되지 않은 데이터 중 가장 작은 '0'을 선택하여 맨 앞 7과 바꿈
# 처리되지 않은 데이터 중 가장 작은 '1'을 선택하여 ~
# 시간복잡도: N번만큼 가장 작은 수를 찾아 맨 앞으로
# N+(N-1)+(N-2)... -> O(N^2)
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i # 가장 앞쪽 인덱스
    for j in range(i+1, len(array)):
        # 작은 숫자를 찾았다면 
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
print(array)
