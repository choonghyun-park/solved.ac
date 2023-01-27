from collections import deque
import sys

dq = deque()

def push_front(X):
    dq.appendleft(X)
 
def push_back(X):
    dq.append(X)
 
def pop_front():
    if empty(): return -1
    else: return dq.popleft()
 
def pop_back():
    if empty(): return -1
    else: return dq.pop()
 
def size():
    return len(dq)
 
def empty():
    if len(dq)==0:return 1
    else: return 0
 
def front():
    if empty():return -1
    else: return dq[0]
 
def back():
    if empty():return -1
    else: return dq[-1]

N = int(sys.stdin.readline())

for i in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0]=="push_front":
        push_front(int(cmd[1]))
    elif cmd[0]=="push_back":
        push_back(int(cmd[1]))
    elif cmd[0]=="pop_front":
        print(pop_front())
    elif cmd[0]=="pop_back":
        print(pop_back())
    elif cmd[0]=="size":
        print(size())
    elif cmd[0]=="empty":
        print(empty())
    elif cmd[0]=="front":
        print(front())
    elif cmd[0]=="back":
        print(back())
