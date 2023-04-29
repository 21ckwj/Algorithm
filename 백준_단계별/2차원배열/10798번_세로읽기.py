array = [[0]*15 for i in range(5)]

for i in range(5):
    row = list(input())
    for j in range(len(row)):
        array[i][j] = row[j]

for i in range(15):
    for j in range(5):
        if array[j][i]==0:
            pass
        else:
            print(array[j][i],end='')
