def divisible(li,k):
    count = 0
    for i in li:
        if(i%k == 0):
            count+=1
    if(count == len(li)):
        return True
    else:
        return False
def factor(lis):
    if(1 in lis):
        return 1
    else:
        miner = min(lis)
        for j in range(miner,0,-1):
            if(divisible(lis,j)):
                return j
s =""
n,q = map(int,input().split())
temp = list(map(int,input().split()))
for i in range(q):
    t,u = map(int,input().split())
    x = min(t,u)
    y = max(t,u)
    if(i == 0):
        s =str(factor(temp[x-1:y]))
    else:
        s = s+"\n"+str(factor(temp[x-1:y]))
print(s)
