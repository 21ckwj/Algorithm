n = int(input())
a = list(map(int,input().split()))

max1 = a[0]
min1 = a[0]

for i in range(n):

    if max1 <= a[i]:
        max1 = a[i]

    if min1 > a[i]:
        min1 = a[i]

print(str(min1)+" "+str(max1))
