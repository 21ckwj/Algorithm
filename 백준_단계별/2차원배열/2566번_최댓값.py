array = []
for i in range(9):
    row = list(map(int,input().split()))
    array.append(row)

# 최댓값 찾기
i=-1
for row in array:
    i +=1
    max_value = max(row)
    max_index = row.index(max_value)
print(max_value)
print(str(i)+' '+str(max_index))

        