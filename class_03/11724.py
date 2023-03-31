import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
# N : 정점의 개수
# M : 간선의 개수

graph = {}
for i in range(1,N+1):
    graph[i] = []

for _ in range(M):
    u,v = map(int,sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

heap = list(range(1,N+1))
cc_cnt = 0
visited = set()
while(heap):
    i = heap.pop()
    # 이미 방문했던 점은 스킵
    if i in visited:
        continue
    # 연결된 점이 없는 경우 바로 제외
    if len(graph[i])==0:
        continue

    cc = set()
    cc_heap = [i]
    while(cc_heap):
        now = cc_heap.pop()
        cc.add(now)
        visited.add(now)
        if len(graph[i])==0: break 
        next = graph[i].pop()
        cc_heap.append(next)
    print(cc)
    cc_cnt += 1

print(cc_cnt)

