d = [0]*100

def fibo(x): # x는 x번째 피보나치 수열

    if x==1 or x==2 :
        return 1
    
    if d[x] != 0:
        return d[x] # 여기가 안떠올랐음
    d[x] = fibo(x-1) + fibo(x-2)
        
    return d[x]

print(fibo(99))
