# 같은눈 3개 -> 10000원+ 같은눈 * 1000원
# 같은눈 2개 -> 1000원 + 같은눈 *100
# 같은눈 x -> 가장큰눈 * 100

a, b , c = map(int,input().split())
# 3개 모두 같은 경우
if (a==b) & (a==c):
    res = 10000 + a*1000

# 2개 모두 같은 경우
elif (a== b) :
    res = 1000 + a* 100

elif (b ==c) :
    res = 1000 + b*100

elif (a==c):
    res = 1000 + c *100
else:
    res = max(a,b,c)*100
print(res)