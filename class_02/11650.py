import sys

N = int(sys.stdin.readline())

dic = {}
keys = []

for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    if x in dic:
        dic[x].append(y)
    else:
        dic[x] = [y]
        keys.append(x)

keys.sort()

for x in keys:
    ys = dic[x]
    ys.sort()
    for y in ys:
        print(x,y)
