#학생 30명, 1~30번
students = [i for i in range(1,31)]

for _ in range(28):
    a = int(input())
    students.remove(a)

print(max(students))
print(min(students))
