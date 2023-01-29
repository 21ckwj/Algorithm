h, m  = map(int,input().split())
t = int(input())

# t 150 -> 2 30
h = h + t//60
m = m + t%60

if m >= 60:
    m = m - 60
    h = h + 1

if h >=24:
    h = h-24

print("%d %d" %(h,m))
