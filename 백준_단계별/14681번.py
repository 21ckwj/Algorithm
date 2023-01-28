x = int(input())
y = int(input())

# x,y >0 1사분면
# x >0, y<0 4사분면
# x <0, y>0 2사분면
# x <0, y<0 3사분면

if x* y > 0:
    if (x>0) or (y>0):
        print(1)
    else:
        print(3)
else:
    if x>0:
        print(4)
    else:
        print(2)


# 이중 for문 보다는 그냥 다 적어주는 편이 나았을 것 같다