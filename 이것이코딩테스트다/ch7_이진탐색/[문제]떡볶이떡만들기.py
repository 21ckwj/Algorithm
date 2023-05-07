# 파라매트릭 서처란
# 최적화 문제를 결정문제("예","아니오")로 바꾸어 해결하는 기법

# 높이 H  H 이상인 떡 잘리고 이하인 떡 안 잘림
# ex. 19 14 10 17 -> 15, 14, 10 ,15
# 4 0 0 2 -> 6cm만큼의 길이를 손님이 가져감
# 손님이 요청한 길이가 M일때 적어도 M만큼의 떡을 얻기위해
# 절단기에 설정할 수 있는 높이의 최댓값 구하는 프로그램?

# 적절한 높이을 찾을 때까지 이진탐색을 수행
# 이높이로 자르면 조건을 만족할 수 있는가? 확인 후
# 탐색 범위를 좁혀서 해결
# 큰 탐색범위(0~10억)을 보면 이진탐색 떠올려야함

# 떡의 개수(N)와 요청한 떡의 길이(M)
n ,m = map(int,input().split())
# 각 떡의 개별 높이
array = list(map(int,input().split()))

# 이진 탐색 시작점 끝점
start = 0
end = max(array)

# 이진 탐색 수정(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start+end)//2
    for x in array:
        # 잘렸을 때의 떡 양 계산
        if x > mid:
            total += x-mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽부분탐색)
    if total < m:
        end = mid-1
    # 떡의 양이 충분한 경우
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 result에 기록
        start = mid +1
    
print(result)

