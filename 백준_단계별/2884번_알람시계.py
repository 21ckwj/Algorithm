# 45분 당기기
# 0:0 ~ 23:59
# 0시 & 45분 이하일 경우 

time = input().split()
hour = int(time[0])
min = int(time[1])

# 0시 45분이하
if (hour ==0) & (min<45) :
    hour = hour +24 -1
    min = min+ 60 - 45

# 0시x , 45분 이상
elif (hour != 0) & (min >=45):
    hour = hour
    min = min -45

# 0시x , 45분 이하
elif (hour !=0) & (min<45):
    hour = hour -1
    min = min + 60 -45

# 0시 45분 이상
else:
    hour = hour
    min = min-45

print(str(hour)+' '+str(min))