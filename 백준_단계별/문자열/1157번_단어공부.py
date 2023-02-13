string = input().upper()

d = dict()
for s in string:
    if s not in d.keys():
        d[s] = 1
    else:
        d[s] +=1

if len([k for k,v in d.items() if max(d.values())==v])==1:
    print(max(d, key=d.get))
else:
    print("?")