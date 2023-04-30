# 나이트는 L자 형태로만 이동가능, 체스판 밖으로 나갈 수 없음
# 수평 2칸 + 수직 1칸
# 수직 2칸 + 수평 1칸
# 말 위치 행 열

location = input()
row = location[0]
col = int(location[1])
rows = ['a','b','c','d','e','f','g','h']

row = rows.index(row)+1

drow = [2,2,-2,-2,1,1,-1,-1]
dcol = [1,-1,1,-1,2,-2,2,-2]

cnt = 0
for r in drow:
    for c in dcol:
        nrow = row + r
        ncol = col + c
        print(nrow,ncol)
    if nrow>8 or ncol>8 or nrow<1 or ncol<1:
        continue
    cnt += 1
    print(cnt)
print(cnt)


