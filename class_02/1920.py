import sys

N = int(sys.stdin.readline().rstrip())
A = set(map(int,sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
X = list(map(int,sys.stdin.readline().rstrip().split()))

for x in X:
    if x in A:
        print(1)
    else:
        print(0)