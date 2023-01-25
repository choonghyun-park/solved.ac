N = int(input())
lst1 = list(map(int,input().split()))
M = int(input())
lst2 = set(map(int,input().split()))

for v2 in lst2:
    print(lst1.count(v2),end=" ")
    