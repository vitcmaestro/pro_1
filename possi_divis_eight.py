def divis(m):
    if(m == 0):
        return False
    if(m%8 == 0):
        return True
    else:
        return False
n= input("")
flag = 0
for i in range(len(n)):
    res = n[i:]
    if(divis(int(res))):
        flag = 1
        break
    res = n[:i]
    if(i!= 0 and divis(int(res))):
        flag = 1
        break
    res =''
    for j in range(len(n)):
        if(i!=j):
            res = res+n[j]
    if(divis(int(res))):
        flag = 1
        break
    res = n[i]
    if(divis(int(res))):
        flag = 1
        break
    
if(flag == 0):
    print("no")
else:
    print("yes")
