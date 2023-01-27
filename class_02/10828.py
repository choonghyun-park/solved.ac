import sys

def push(stack,X):
    stack.append(X)
    return stack

def pop(stack):
    if empty(stack):return -1
    return stack.pop()

def size(stack):
    return len(stack)
    
def empty(stack):
    if len(stack)==0:return 1
    else: return 0

def top(stack):
    if empty(stack):return -1
    else: return stack[-1]

stack = []

N = int(sys.stdin.readline())
for _ in range(N):
    commends = sys.stdin.readline().rstrip().split()
    if len(commends)>2:
        print("Something wrong")
    elif len(commends)==2:
        assert commends[0] == "push"
        stack = push(stack,int(commends[1]))        
    else:
        commend = commends[0]
        if commend=="pop":
            print(pop(stack))
        elif commend=="size":
            print(size(stack))
        elif commend=="empty":
            print(empty(stack))
        elif commend=="top":
            print(top(stack))


