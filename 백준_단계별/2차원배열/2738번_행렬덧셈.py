n,m = map(int,input().split())

A, B = [],[]
for _ in range(n):
    row = list(map(int,input().split()))
    A.append(row)

for _ in range(n):
    row = list(map(int,input().split()))
    B.append(row)

for row in range(n):
    for col in range(m):
        value = A[row][col]+ B[row][col]
        print(value,end=' ')
    print()
    
    
