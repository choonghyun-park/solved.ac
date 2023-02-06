import sys
from collections import deque

def sum_2d(lst):
    s = 0
    for l in lst:
        s+=sum(l)
    return s

N = int(sys.stdin.readline())

paper=[]
for _ in range(N):
    line = list(map(int,sys.stdin.readline().split()))
    paper.append(line)

dq = deque([])

dq.append(paper)
sub = [(0,0),(1,0),(0,1),(1,1)]

white=0
blue=0

while(dq):
    p = dq.popleft()
    w = len(p)
    if sum_2d(p)==w**2:
        blue+=1
    elif sum_2d(p)==0:
        white+=1
    else:    
        for s in sub:
            sub_p = []
            sub_w = int(w*1/2)
            for i in range(s[0]*sub_w,(s[0]+1)*sub_w):
                sub_p.append(p[i][s[1]*sub_w:(s[1]+1)*sub_w])

            dq.append(sub_p)
    
print(white)
print(blue)

