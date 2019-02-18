m,n = map(int,input().split())
coins = list(map(int,input().split()))
coins = sorted(coins)
tot = 0
for i in range(m-1,-1,-1):
    if(n>0 and coins[i]<=n):
        tot = tot + n//coins[i]
        n = n%coins[i]
print(tot)
