# 1 -> 2초
# 2 ABC-> 3초 
# 3 DEF -> 4초 ..
# 3 3 3 3 3 3 4 4 4

words = input()
dials = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

res = 0
for w in words:
    for i in range(len(dials)):
        if w in dials[i]:
            res += i+3
print(res)
