# N*M 미로 괴물을 피해 탈출해야함
# 위치는 (1,1) 미로의 출구는 (N,M) 한번에 한칸식 이동
# 괴물있는부분 0, 없는부분 1
# 탈출하기 위해 움직여야 하는 최소 칸의 개수?
# 시작칸 , 마지막 칸 모두 포함

# BFS 시작지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색
# 상하좌우 모든 거리 1로 동일

from collections import deque

n,m = map(int,input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 이동할 네가지 방향 정의 (상,하, 좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    # 큐 구현
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue.popleft():
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or nx>=n or ny<0 or ny >=m:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단거리기록
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))
