import sys

def isDecimal(n):
    # 1 is not Decimal
    if n==1:return False

    # check wether n is divided by smaller number than n
    for i in range(2,n):
        if n%i==0:return False
    return True

N = int(input())
inputs = list(map(int,sys.stdin.readline().rstrip().split()))

cnt = 0
for input in inputs:
    if isDecimal(input):cnt+=1

print(cnt)