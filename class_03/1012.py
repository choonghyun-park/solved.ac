import sys
from collections import deque

def printGround(ground):
    for g in ground:
        print(g)
    print()

T = int(sys.stdin.readline()) # 테스트 케이스 수

neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
cnt_areas = []

for _ in range(T):
    M,N,K = map(int,sys.stdin.readline().split()) # 가로, 세로, 배추의 개수
    ground = [[0 for w in range(N)] for h in range(M)]

    # 배추가 있는 영역을 표시
    for _ in range(K):
        X,Y = map(int,sys.stdin.readline().split())
        ground[X][Y] = 1
    
    # 분리된 영역의 수를 계산
    cnt_area = 0
    for m in range(M):
        for n in range(N):
            if ground[m][n]<=0:
                continue
            
            cnt_area += 1
            targets = deque([(m,n)])
            ground[m][n] = -1
            while(targets):
                # printGround(ground)
                target = targets.popleft()
                for neighbor in neighbors:
                    x = target[0] + neighbor[0]
                    y = target[1] + neighbor[1]
                    if x<0 or x>=M or y<0 or y>=N:continue
                    if ground[x][y]==1:
                        targets.append((x,y))
                        ground[x][y]=-1
    cnt_areas.append(cnt_area)

for cnt_area in cnt_areas:print(cnt_area)
