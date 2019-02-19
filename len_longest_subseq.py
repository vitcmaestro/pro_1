n = int(input())
lis = list(map(int,input().split()))
maxer = 0
count = 1
for i in range(1,n):
    if(lis[i]>=lis[i-1]):
        count+=1
        if(count> maxer):
            maxer = count
    else:
        count = 0
print(maxer)
