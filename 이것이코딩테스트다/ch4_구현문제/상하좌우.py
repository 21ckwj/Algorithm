# 여행가는 N*N 정사각형 가장 왼쪽 위 (1,1)에 서있음
# L R U D 이동
# 정사각형 벗어나면 무시

n = int(input())
move = list(input().split())
# L R U D
directions = ["L","R","U","D"]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

x=1
y=1
for m in move:
    i = directions.index(m)
    x += dx[i]
    y += dy[i]
    if (x>=n) or (x<=0) or (y<=0) or (y>=n):
        x -= dx[i]
        y -= dy[i]
    print(str(x)+' '+str(y))

# print(str(x)+' '+str(y))