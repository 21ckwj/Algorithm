# 500원 100원 50원 10원 거스름돈 사용
# 거스를 돈 N (10의배수)일때 거슬러줘야 할 동전 최소개수

n = int(input())
coins = [500,100,50,10]
total = 0
for coin in coins:
    coin_num = n//coin
    remain = n%coin
    n = remain
    total += coin_num
print(total)

