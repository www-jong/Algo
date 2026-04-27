from collections import deque
import sys
input=sys.stdin.readline
d=[0,0,1,-1]

def drop(s,tar):
    flag=0
    while True:
        for i in range(len(tar)):
            li[tar[i][0]][tar[i][1]]='.'
            tar[i]=[tar[i][0]+1,tar[i][1]]
            li[tar[i][0]][tar[i][1]]='x'

        for x,y in tar:
            if (x+1,y) in s:
                return

    pass

def func():
    s=set()
    q=deque()
    visit=[[0]*(C) for _ in range(R+2)]
    for i in range(C):
        q.append((R+1,i))
        visit[R+1][i]=1
        s.add((R+1,i))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if 1<=nx<=R and 0<=ny<C and li[nx][ny]=='x' and not visit[nx][ny]:
                q.append((nx,ny))
                visit[nx][ny]=1
                s.add((nx,ny))

    q=deque()
    visit=[[0]*(C) for _ in range(R)]
    tar=[]
    for i in range(1,R):
        for j in range(C):
            if li[i][j]=='x' and (i,j) not in s:
                q.append((i,j))
                visit[i][j]=1
                tar.append((i,j))
                break
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+d[i],y+d[3-i]
            if 1<=nx<=R and 0<=ny<C and li[nx][ny]=='x' and not visit[nx][ny] and (nx,ny) not in s:
                q.append((nx,ny))
                visit[nx][ny]=1
                tar.append((nx,ny))
    if not tar:
        return
    tar.sort(key=lambda x:-x[0])
    drop(s,tar)


R,C=map(int,input().split())
li=[[0]]+[list(input().rstrip()) for _ in range(R)]+[['x']*C]


N=int(input())
shoot=list(map(lambda x: R+1-int(x),input().split()))

for i in range(N):
    if i%2==0:
        for j in range(C):
            if li[shoot[i]][j]=='x':
                li[shoot[i]][j]='.'
                break
    else:
        for j in range(C-1,-1,-1):
            if li[shoot[i]][j]=='x':
                li[shoot[i]][j]='.'
                break
    func()

for i in li[1:-1]:
    print(*i,sep="")
