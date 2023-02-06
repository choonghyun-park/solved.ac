import sys
from collections import deque

coms = {}

def connect(com1,com2):
    if com1 in coms:
        coms[com1].append(com2)
    else:
        coms[com1]=[com2]
    if com2 in coms:
        coms[com2].append(com1)
    else:
        coms[com2]=[com1]
        

N = int(sys.stdin.readline())
P = int(sys.stdin.readline())


for _ in range(P):
    com1,com2 = map(int,sys.stdin.readline().split())
    connect(com1,com2)

dq = deque()
virus = []

dq.append(1)
while(dq):
    c = dq.popleft()
    if c not in coms:continue
    nexts = coms[c]
    # 방문한 노드는 삭제
    del(coms[c])
    for next in nexts:
        virus.append(next)
        dq.append(next)
virus = set(virus)
print(len(virus)-1) # 1은 제외
    