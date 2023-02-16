# A = 고정비용
# B = 가변비용
# C = 책정가격

a,b,c = map(int,input().split())
if c-b <= 0:
    print(-1)
else:
    print(int(a/(c-b))+1)

# a + b* n < c *n

# (c-b)*n > a

# n > a/(c-b)

