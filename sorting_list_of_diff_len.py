n = int(input(""))
ans = []
for i in range(n):
    temp = list(map(int,input().split()))
    for i in temp:
        ans.append(i)
print(" ".join(map(str,sorted(ans))))
    
