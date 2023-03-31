import sys

M = int(sys.stdin.readline())

S = set()

outputs = []

for _ in range(M):
    input = sys.stdin.readline().rstrip().split()

    st = input[0]
    if len(input)>1:
        x = int(input[1])

    if st=="add":
        if x not in S:
            S.add(x)
    elif st=="remove":
        if x in S:
            S.discard(x)
    elif st=="check":
        if x in S: 
            print(1)
            # outputs.append(1)
        else: 
            print(0)
            # outputs.append(0)
    elif st=="toggle":
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif st=="all":
        S = set(range(1,21))
    elif st=="empty":
        S = set()

# for o in outputs:
#     print(o)