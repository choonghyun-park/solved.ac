import heapq
import sys

N = int(sys.stdin.readline())
inputs = []
heap = []

for _ in range(N):
    input = int(sys.stdin.readline())
    inputs.append(input)
    
for input in inputs:
    if input==0:
        # 만약 배열이 비어있는 경우는 0을 출력
        if len(heap)==0:
            print(0)
        # 배열에서 가장 큰 값 출력하고 그 값을 배열에서 제거
        else:
            print(-heapq.heappop(heap))

    else:
        # 배열에 input을 추가
        heapq.heappush(heap,-input)
    
