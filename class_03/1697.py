import sys
from collections import deque

memory_mvs = {}

def moves(X):
    if X in memory_mvs:return memory_mvs[X]
    mvs = []
    if X-1 >= 0 and X-1 <=100000:
        mvs.append(X-1)
    if X+1 >= 0 and X+1 <=100000:
        mvs.append(X+1)
    if 2*X >= 0 and 2*X <=100000:
        mvs.append(2*X)
    memory_mvs[X]=mvs
    return mvs

N,K = map(int,sys.stdin.readline().split())

dq = deque()
dq.append([N])
time = 0
found = False

while(dq):
    # print(dq)
    if N==K: break
    if found:break
    time += 1   
    dq_copy = dq.copy()
    dq.clear()
    for next_mvs in dq_copy:
        if found:break
        for next_mv in next_mvs:
            if next_mv in memory_mvs:continue
            mvs = moves(next_mv)
            if K in mvs:
                found = True
                break
            dq.append(mvs)
print(time)    