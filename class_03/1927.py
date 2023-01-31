import sys
import heapq

heap = []
ans = []

def push(heap,x):
    heapq.heappush(heap,x)

def pop(heap):
    if len(heap)==0:
        return 0
    return heapq.heappop(heap)
    

N = int(sys.stdin.readline())

for _ in range(N):
    x = int(sys.stdin.readline())
    if x>0:
        push(heap,x)
    elif x==0:
        ans.append(pop(heap))
    
for a in ans:
    print(a)
    