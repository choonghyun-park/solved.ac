import sys

N,M = map(int,sys.stdin.readline().split())

no_hear = []
no_hear_see = []

for _ in range(N):
    input = sys.stdin.readline().rstrip()
    no_hear.append(input)

no_hear = set(no_hear)
for _ in range(M):
    input = sys.stdin.readline().rstrip()
    if input in no_hear:
        no_hear_see.append(input)

no_hear_see = sorted(no_hear_see)

print(len(no_hear_see))
for v in no_hear_see:
    print(v)