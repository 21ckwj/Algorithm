# 다익스트라 최단 경로 알고리즘

# 특정 노드에서 다른 모든 노드로 가는 최단경로 계산
# 음의 간선이 없을 때 정상 작동
# 그리디 알고리즘으로 분류

# 1. 출발노드 설정
# 2. 최단거리 테이블을 초기화 
# 3. 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용계산하여 최단 거리 테이블 갱신
# 5. 위 과정 3번과 4번 반복

# 단계를 거치며 한번 처리된 노드의 최단거리 정보 저장

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한 의미하는 값으로 10억 설정

# 노드개수, 간선개수
n,m = map(int,input().split())

# 시작노드 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드 정보 담는 리스트
graph = [[] for i in range(n+1)]

# 방문 기록
visited = [False] * (n+1)

# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

# 방문하지 않은 노드 중, 가장 최단거리가 짧은 노드번호 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라
def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[i]
