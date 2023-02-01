lst = []
for i in range(9):
    a= int(input())
    lst.append(a)

b = max(lst)
print(b)

for i in range(9):
    if b == lst[i]:
        print(i+1)