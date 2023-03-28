import sys
from queue import PriorityQueue
from collections import deque

MAX = 1
MIN = -1
MAX_Q = PriorityQueue()
MIN_Q = PriorityQueue()
NUMS = {}
LEN_Q = 0

def insert(n):
    global MAX,MIN,MAX_Q,MIN_Q,NUMS,LEN_Q
    if n in NUMS:
        NUMS[n]+=1
    else:
        NUMS[n]=1
    MAX_Q.put((-n,n))
    MIN_Q.put((n,n))
    LEN_Q += 1

def pop(sign):
    global MAX,MIN,MAX_Q,MIN_Q,NUMS,LEN_Q
    while(1):
        # 빈 Q일 경우 함수를 반환
        if empty():return
        
        if sign==MAX:
            n = MAX_Q.get()[1]
        elif sign==MIN:
            n = MIN_Q.get()[1]
        
        if n in NUMS and NUMS[n]>0:
            NUMS[n]-=1
            LEN_Q -= 1
            return n

def empty():
    if LEN_Q==0:return True
    else: return False

def clear():
    global MAX,MIN,MAX_Q,MIN_Q,NUMS,LEN_Q
    MAX_Q = PriorityQueue()
    MIN_Q = PriorityQueue()
    NUMS = {}
    LEN_Q = 0

T = int(sys.stdin.readline())

ans = []
for _ in range(T):
    k = int(sys.stdin.readline())
    clear()
    for _ in range(k):
        op,n = sys.stdin.readline().split()
        n = int(n)
        if op=="I":
            insert(n)
        elif op=="D":
            pop(n)
    if LEN_Q==0:
        ans.append("EMPTY")
    elif LEN_Q==1:
        p = pop(MAX)
        ans.append((p,p))
    else:
        ans.append((pop(MAX),pop(MIN)))

for a in ans:
    if a=="EMPTY":    
        print(a)
    else:
        print(a[0],a[1])