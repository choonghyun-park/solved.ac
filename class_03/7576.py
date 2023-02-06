import sys
from collections import deque

def sum_2d(lst):
    s = 0
    for l in lst:
        s+=sum(l)
    return s

def printBox(box):
    for b in box:
        print(b)
    print()

M,N = map(int,sys.stdin.readline().split())

box = []
dq = deque([])
full_score = 0
empty = 0

for i in range(N):
    line = list(map(int,sys.stdin.readline().split()))
    for j,t in enumerate(line):
        if t==1:dq.append((i,j))
        elif t==-1:empty+=1
    box.append(line)
neighbor = [(1,0),(0,1),(-1,0),(0,-1)]

if sum_2d(box)+empty*2==N*M:
    print(0)
    exit()

cycle_counter = len(dq)
date = 0

while(dq):
    tomato = dq.popleft()
    cycle_counter-=1
    for n in neighbor:
        x = tomato[0]+n[0]
        y = tomato[1]+n[1]
        if x>=N or x<0 or y>=M or y<0:
            continue
        n_tomato = box[x][y]
        if n_tomato==0:
            dq.append((x,y))
            box[x][y]=1
    if cycle_counter==0:
        # print("dq",dq)
        cycle_counter=len(dq)
        date+=1
        # printBox(box)

full_score=sum_2d(box)
if full_score+empty*2 == M*N:
    print(date-1)
else:
    print(-1)
