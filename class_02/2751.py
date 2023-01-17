import sys
N = int(input())
inputs = []
for i in range(N):
    input = int(sys.stdin.readline().rstrip())
    inputs.append(input)
inputs.sort()
for input in inputs:print(input)