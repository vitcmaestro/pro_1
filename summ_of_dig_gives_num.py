def sumofdig(y):
    adr = 0
    while(y>0):
        rem = y%10
        adr = adr+rem
        y = y//10
    return adr
n = int(input(""))
c = 0
ans = []
for i in range(1,n):
    x = sumofdig(i)
    add = x+i
    if(add == n):
        ans.append(i)
        c+=1
print(c)
for i in ans:
    print(i)
