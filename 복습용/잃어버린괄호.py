# input ex. 55-50+40, 10+20+30+40, 00009-00009, 10-20-20+30
# output: 최소로 만드는 값 ex. -35

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

    

