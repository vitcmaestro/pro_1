n = int(input(""))
a = list(map(int,input().split()))
for i in range(1,n):
    sum1 = sum(a[:i])
    sum2 = sum(a[i:])
    avg1 = sum1/i
    avg2 = sum2/(n-i)
    if(avg1 == avg2):
        print("yes")
        break
else:
    print("no")
