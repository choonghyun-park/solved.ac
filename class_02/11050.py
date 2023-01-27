import sys

def factorial(N):
    if N==0:return 1
    elif N==1:return 1
    elif N>1 : return N*factorial(N-1)

N,K = map(int,sys.stdin.readline().split())

nCk = int(factorial(N) / (factorial(K)*factorial(N-K)))

print(nCk)