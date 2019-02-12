def prevsum(j):
    ret  = 0
    for x in range(j):
        if(res[x] < res[j]):
            ret = ret+ res[x]
    return ret
n = int(input(""))
res = list(map(int,input().split()))
s = 0
ans = 0
for i in range(1,n):
    s = prevsum(i)
    ans = ans+s
print(ans)
