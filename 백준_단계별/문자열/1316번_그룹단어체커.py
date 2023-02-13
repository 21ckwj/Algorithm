# n = int(input())
# group_word = 0
# for _ in range(n):
#     words = input()
#     button = 0
#     for i in range(len(words)-1):
#         if words[i] == words[i+1]:
#             pass
#         else:
#             if words[i] in words[i+1:]:
#                 button =1

#     if button ==0:
#         group_word +=1

# print(group_word)

N=int(input())
cnt=0
for i in range(N):
    word = input()  
    bl_=True
    for j in range(len(word)-1):
        if word[j]!=word[j+1]:
            if word[j] in word[j+1:]:
                bl_=False
                break
    if bl_:
        cnt+=1
print(cnt)