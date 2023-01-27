from collections import deque
import sys

queue = deque()

def push(X):
    queue.append(X)
    return

def pop():
    if empty():
        return -1
    else:
        return queue.popleft()

def size():
    return len(queue)

def empty():
    if len(queue)==0:return 1
    else:return 0

def front():
    if empty():return -1
    return queue[0]

def back():
    if empty():return -1
    return queue[-1]

N = int(sys.stdin.readline())

for i in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0]=="push":
        push(int(cmd[1]))
    elif cmd[0]=="pop":
        print(pop())
    elif cmd[0]=="size":
        print(size())
    elif cmd[0]=="empty":
        print(empty())
    elif cmd[0]=="front":
        print(front())
    elif cmd[0]=="back":
        print(back())

    