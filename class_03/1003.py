import sys

d = [0]*50
d[1] = 1

cnt_0 = 0
cnt_1 = 0
cnts = {}
cnts[0] = (1,0)
cnts[1] = (0,1)
lst = []

def fibonacci(n):
    global cnt_0,cnt_1
    if n==0:
        cnt_0 += 1
        return 0
    elif n==1:
        cnt_1 += 1
        return 1
    if d[n] != 0:
        cnt_0 += cnts[n][0]
        cnt_1 += cnts[n][1]
        return d[n]
    
    d[n] = fibonacci(n-1)+fibonacci(n-2)
    cnts[n] = (cnt_0,cnt_1)
    return d[n]

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    cnt_0 = 0
    cnt_1 = 0
    fn = fibonacci(N)
    lst.append(N)

for n in lst:
    print(cnts[n][0],cnts[n][1])