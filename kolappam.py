n = int(input(""))
li = list(map(int,input().split()))
count = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if(li[i]<li[j]<li[k]):
                count+=1
print(count)
