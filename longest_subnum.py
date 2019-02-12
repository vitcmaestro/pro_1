num,k = map(int,input().split())
res= []
s = str(num)
for i in range(k):
    first = i
    last = i+k
    x = s[first:last]
    res.append(x)
print(min(res))
