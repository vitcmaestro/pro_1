n = int(input(""))
li = list(map(int,input().split()))
maxer = 0
for i in range(n):
    x = sum(li[i::2])
    if(x > maxer):
        maxer = x
print(maxer)
    
