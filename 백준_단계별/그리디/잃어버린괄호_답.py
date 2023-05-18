a = input().split('-')
num = []
for i in a:
    plus = 0
    plus_nums = i.split("+")
    for p in plus_nums:
        plus += int(p)
    num.append(plus)

ans = num[0]
for plus in num[1:]:
    ans -= plus

print(ans)
