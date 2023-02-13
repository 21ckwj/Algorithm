string = input().upper()
alphabets = list(set(string))

# 각 알파벳의 개수 리스트에 넣기
cnt_lst = []
for a in alphabets:
    cnt = string.count(a)
    cnt_lst.append(cnt)

# 리스트에 모은 개수들 중 최대값이 중복된다면
if cnt_lst.count(max(cnt_lst))>1:
    print("?")

# 중복 없을 경우
else:
    max_index = cnt_lst.index(max(cnt_lst)) # 횟수 리스트의 가장 큰 숫자의 인덱스
    print(alphabets[max_index])