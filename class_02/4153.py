import sys

def isRightTri(a,b,c):
    lst=[a,b,c]
    lst.sort()
    if lst[2]**2 == lst[0]**2+lst[1]**2:return True
    else: return False

inputs=[]

while(1):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    if a==0 and b==0 and c==0:break
    inputs.append((a,b,c))

for input in inputs:
    a,b,c = input
    if isRightTri(a,b,c):print("right")
    else:print("wrong")