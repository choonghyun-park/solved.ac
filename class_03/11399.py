import sys
import heapq


N = int(sys.stdin.readline())

P = map(int,sys.stdin.readline().rstrip().split())

heap = []

for pi in P:
    heapq.heappush(heap,pi)

sum = 0
n = len(heap)
for i in range(n):
    sum += heapq.heappop(heap) * (n-i)

print(sum)