# 파이썬의 경우 최대 재귀깊이가 있어 오류남
def recursive_fuction():
    print("재귀함수를 호출합니다")
    recursive_fuction()

# recursive_fuction()

# 종료 조건을 포함한 재귀함수 예제
def recursive_fuction(i):
    if i ==100:
        return
    print(i,'번째 재귀함수에서',i+1, '번째 재귀함수를 호출합니다.')
    recursive_fuction(i+1)
    print(i, "번째 재귀함수를 종료합니다.")
recursive_fuction(1)