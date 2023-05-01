# N*M 크기의 얼음틀, 구멍 뚫려있는부분 0, 칸막이부분 1.
# 구멍이 뚫려있는 부분끼리는 상하좌우 부터 있는 경우
# 서로 연결되어 있는 것으로 간주

# 얼음 틀의 모양이 주어졋을 때 생성되는 총 아이스크림의 개수?

# 1.특정지점 상하좌우 살피고 주변 지점중 값이 0이면서 아직 방문않은 지점
# 있을 시 방문

# 2. 방문한 지점에서 다시 상하좌우 살피며 방문
# 3. 1,2과정을 반복하며, 방문하지 않은 지점의 수를 카운트

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# DFS로 특정노드를 방문, 연결된 모든 노드들도 방문
def dfs(x,y):
    # 현재위치가 주어진 범위를 벗어나는 경우 즉시 종료
    if x <=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 현재노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1 
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    # graph[x][y] != 0 이면(진입 x일 경우)
    return False

result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        # 
        if dfs(i,j) ==True:
            result +=1
print(result) 