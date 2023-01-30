import sys

def printMap(map):
    for m in map:
        print(m)
    print()

def relocate(N,r,c):
    if N==1:
        if r==0 and c==0:order=0
        elif r==0 and c==1:order=1
        elif r==1 and c==0:order=2
        elif r==1 and c==1:order=3
        return order
    if r<pow(2,N-1) and c<pow(2,N-1):
        # area 1
        order = pow(4,N-1)*0
        sub_r = r
        sub_c = c
    elif r<pow(2,N-1) and c>=pow(2,N-1):
        # area 2
        order = pow(4,N-1)*1
        sub_r = r
        sub_c = c - pow(2,N-1)
    elif r>=pow(2,N-1) and c<pow(2,N-1):
        # area 3
        order = pow(4,N-1)*2
        sub_r = r - pow(2,N-1)
        sub_c = c 
    elif r>=pow(2,N-1) and c>=pow(2,N-1):
        # area 4
        order = pow(4,N-1)*3
        sub_r = r - pow(2,N-1)
        sub_c = c - pow(2,N-1)
    
    return order + relocate(N-1,sub_r,sub_c)

N,r,c = map(int,sys.stdin.readline().split()) # r:row, c:column

print(relocate(N,r,c))

