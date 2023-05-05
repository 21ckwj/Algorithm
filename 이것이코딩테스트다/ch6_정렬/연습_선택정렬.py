array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    for j in range(i+1, len(array)):
        # 가장 첫번째 보다 작으면
        if array[i] > array[j]:
            array[i],array[j] = array[j], array[i]

        else:
            continue
print(array)