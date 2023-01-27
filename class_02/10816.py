import sys

N = int(sys.stdin.readline().rstrip())
lst1 = list(map(int,sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
lst2 = list(map(int,sys.stdin.readline().rstrip().split()))

dict1 = {}

for v in lst1:
    if v not in dict1:dict1[v]=1
    else: dict1[v]+=1

for v in lst2:
    if v not in dict1:print("0",end=" ")
    else:print(dict1[v],end=" ")
