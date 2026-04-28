from collections import deque
import sys
d=[(1,0),(0,-1),(0,1)]
input=sys.stdin.readline

N,M=map(int,input().split())
MIN=-float('inf')
li=[list(map(int,input().split())) for _ in range(N)]

dp=[[[MIN,MIN] for _ in range(M)] for _ in range(N)]
dp[0][0]=[li[0][0],li[0][0]]

for i in range(1,N):
    dp[i][0][0]=dp[i-1][0][0]+li[i][0]
    dp[i][0][1]=dp[i-1][0][1]+li[i][0]

for i in range(N):
    for j in range(M):
        if 0<=i-1<N:
            dp[i][j][0]=max(dp[i-1][j])+li[i][j]
            dp[i][j][1]=max(dp[i-1][j])+li[i][j]
    for j in range(1,M):
        dp[i][j][1]=max(dp[i][j-1][1]+li[i][j],dp[i][j][1])
    for j in range(M-2,-1,-1):
        dp[i][j][0]=max(dp[i][j+1][0]+li[i][j],dp[i][j][0])

print(max(dp[N-1][M-1]))