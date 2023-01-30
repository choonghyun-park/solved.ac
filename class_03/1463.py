import sys
from collections import deque

memory = {}

def outputs(X):
    global memory
    if X in memory:
        return memory[X]
    outs = []
    if X%3==0:
        outs.append(int(X/3))
    if X%2==0:
        outs.append(int(X/2))
    if X>1:
        outs.append(X-1)
    memory[X]=outs
    return outs

X = int(sys.stdin.readline())
cnt = 0
dq = deque([])
dq.append([X])
find_1 = False

while(dq and X!=1):
    # print(dq)
    dq_copy = dq.copy()
    dq.clear()
    # calculate next outputs
    if find_1:break   
    cnt+=1
    for before_outs in dq_copy:
        if find_1:break
        for before_out in before_outs:
            outs = outputs(before_out)
            dq.append(outs)
            if 1 in outs:
                find_1=True
                break
print(cnt)
    





