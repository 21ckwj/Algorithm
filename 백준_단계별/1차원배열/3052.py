lst = []
for i in range(10):
    n = int(input())
    m = n%42
    lst.append(m)

print(len(set(lst)))