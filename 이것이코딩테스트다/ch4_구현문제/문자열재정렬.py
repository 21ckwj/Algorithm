# 알파벳 대문자와 숫자(0~9) 로만 구성된 문자열이 입력으로 주어짐
# 이때 모든 알파벳을 오름차순 정렬로 출력한 뒤, 그 뒤 모든 술자를 더한값을
# 이어서 출력
# ex. K1KA5CB7 -> ABCKK13 출력

input_str = input()
numbers = [str(i) for i in range(10)]

num_list = []
alpha_list = []

for i in input_str:
    if i in numbers:
        num_list.append(int(i))
    else:
        alpha_list.append(i)

# 알파벳 차례로 정렬
alpha_list.sort()

# 숫자합
sum = sum(num_list)

print(''.join(alpha_list)+str(sum))