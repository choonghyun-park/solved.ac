import sys

T = int(input())

inputs = []
for i in range(T):
    H,W,N = map(int,sys.stdin.readline().rstrip().split())
    inputs.append((H,W,N))

for input in inputs:
    h,w,n = input 
    '''
    h : number of floor
    w : w rooms in a floor
    n : nth person
    '''

    floor = n%h
    room = n//h+1
    if floor==0 : 
        floor=h
        room =n//h
    print(100*floor+room)
    