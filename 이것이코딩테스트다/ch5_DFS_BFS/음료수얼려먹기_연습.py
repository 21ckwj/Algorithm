n,m = 4,5
graph = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]

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


print(dfs(0,0))
print(dfs(0,1))
print(dfs(0,2))
print(dfs(0,3))
print(dfs(0,4))
print('\n')
print(dfs(1,0))
print(dfs(1,1))
print(dfs(1,2))
print(dfs(1,3))
print(dfs(1,4))
print('\n')
print(dfs(2,0))
print(dfs(2,1))
print(dfs(2,2))
print(dfs(2,3))
print(dfs(2,4))
print('\n')
print(dfs(3,0))
print(dfs(3,1))
print(dfs(3,2))
print(dfs(3,3))
print(dfs(3,4))
print('\n')