import sys

def isInt(x):
    try:
        assert(int(x))
        return True
    except:return False

N,M = map(int,sys.stdin.readline().split())

dogam_1 = {}
dogam_2 = {}

ans = []

for i in range(1,N+1):
    pckmon = sys.stdin.readline().rstrip()
    dogam_1[i]=pckmon
    dogam_2[pckmon]=i

for _ in range(M):
    input = sys.stdin.readline().rstrip()
    if isInt(input):
        ans.append(dogam_1[int(input)])
    else: 
        ans.append(dogam_2[input])

for a in ans:
    print(a)