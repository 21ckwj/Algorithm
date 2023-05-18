# 괄호를 지우고 다시 괄호를 쳐서 가장 최솟값을 만드는 프로그램 작성
# +끼리 먼저 묶어야 작아질 것 같다

# 10 - 20 + 30 -40 + 20
# 10 - (20 + 30) -40 + (20)

# 9 - 10 - 11

nums = input()

# '-' 기준으로 split
if '-' in nums:
    split_list = nums.split('-')
    
    plus = int(split_list[0])
    minus = 0
    for nums in split_list[1:]:
        # + 있으면 더해서 빼줄 값
        if '+' in nums:
            n1, n2 = map(int,nums.split('+'))
            minus += n1+n2

        # + 기호 없으면 다 빼주면 됨
        else:
            minus += int(nums)
    
    ans = plus - minus

else:
    split_list = list(map(int,nums.split('+')))
    ans = sum(split_list)

print(ans)
    
# 런타임 에러 ㅠㅠ




