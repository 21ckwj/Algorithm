a,b = input().split()
text1 = ""
for i in a[::-1]:
    text1 += i

text2 = ""
for i in b[::-1]:
    text2 += i

if int(text1) > int(text2):
    print(text1)
else:
    print(text2)