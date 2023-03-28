import sys

Q = {}
def insert(n):
    Q[n]=n

def delete(n):
    if n==1: # delete max
        keys = list(Q.keys())
        if len(keys)!=0:
            del(Q[max(keys)])
    elif n==-1: # delete min
        keys = list(Q.keys())
        if len(keys)!=0:
            del(Q[min(keys)])

    if n in Q:
        del(Q[n])

T = int(sys.stdin.readline())

ans = []
for _ in range(T):
    k = int(sys.stdin.readline())
    for _ in range(k):
        op,n = sys.stdin.readline().split()
        n = int(n)
        if op=="I":
            insert(n)
        elif op=="D":
            delete(n)

    keys = list(Q.keys())
    if len(keys)==0:
        ans.append("EMPTY")
    else:
        keys.sort()
        ans.append((keys[-1],keys[0]))

for a in ans:
    if type(a)=="tuple":    
        print(a[0],a[1])
    else:
        print(a)