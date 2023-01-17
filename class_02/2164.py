from collections import deque

N = int(input())
deq = deque(range(1,N+1))

splash = True

while(len(deq)>1):
    # print("deque state :",deq)
    if splash:
        deq.popleft()
        splash=False
    else:
        moveCard = deq.popleft()
        deq.append(moveCard)
        splash=True

print(deq[0])

