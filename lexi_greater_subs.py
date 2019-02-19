x= input("")
ans =""
for i in range(1,len(x)):
    if(x[i] > x[0]):
        ans = x[i:]
print(ans)
