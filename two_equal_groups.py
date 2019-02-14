n,a,b = map(int,input().split())
for i in range(0,n+1,2):
    x = a*i
    rem = n-x
    y = rem//(2*b)
    if(x+b*y == n):
        print("YES")
        break
else:
    print("NO")
