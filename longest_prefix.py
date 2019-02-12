def finder(a,b):
    cmn = ""
    leng = min(a,b)
    for i in range(len(leng)):
        if(a[i] == b[i]):
            cmn = cmn+a[i]
        else:
            break
    return cmn
n = int(input(""))
res = []
for i in range(n):
    x = input("")
    res.append(x)
start = res[0]
for i in range(1,n):
    start = finder(start,res[i])
print(start)
