import math
n = int(input(""))
i = 1
ans = 0
m = 0
while(i<=n):
    ans = i
    i = 2**m
    m+=1
print(n-ans)
