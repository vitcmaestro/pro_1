n = int(input())
x = 1
y = str(bin(x))
ans = []
fin =[]
res =[]
z = 1
while(len(y) <= n+2):
    ans.append(y[2:])
    x+=1
    y = str(bin(x))
while(len(ans) >0 and z<=n):
    i = 0
    while(len(ans)>0 and i<len(ans)):
        if(ans[i].count('1') == z):
            fin.append(ans[i])
            ans.remove(ans[i])
        else:
            i+=1
    z+=1
    res.append(fin)
    fin =[]

for i in res:
    for j in i:
        if(len(j) < n):
            x= n-len(j)
            y = "0"*x
            j = y+j
        print(j)
