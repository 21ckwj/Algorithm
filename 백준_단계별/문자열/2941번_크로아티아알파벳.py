c_list =["c=","c-","dz=","d-","lj","nj","s=","z="]

string = input()
for c in c_list:
    if c in string:
        string = string.replace(c,'*')
print(len(string))


