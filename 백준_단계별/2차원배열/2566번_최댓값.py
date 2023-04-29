array = []
for i in range(9):
    row = list(map(int,input().split()))
    array.append(row)

# 최댓값 + 위치 찾기
max_lst = []
for i in range(9):
    row_max = max(array[i])
    max_idx = array[i].index(row_max) +1

    max_lst.append(row_max)

    if row_max == max(max_lst):
        real_max = row_max
        real_idx = max_idx
        real_col = i+1 
print(real_max)
# 행 렬
print(str(real_col)+' '+str(real_idx))



    

        