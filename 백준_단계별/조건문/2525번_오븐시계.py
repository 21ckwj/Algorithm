# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때,
#  오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오

hour, min = map(int,input().split())
time = int(input())

# hour 23 22 .. -> 0
# time -> hour + min 

# ex. 80 -> 1 + 20
time_h = time//60
time_m = time%60

min = min + time_m

if (min >= 60):
    min_ = min%60
    hour_ = hour + time_h + min//60

    if hour_ >= 24 :
        hour_ = hour_ -24

elif (min < 60):
    min_ = min % 60
    hour_ = hour + time_h

    if hour_ >= 24 :
        hour_ = hour_ -24

print(str(hour_)+' '+str(min_))



