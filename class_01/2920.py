lst = list(map(int,input().split()))
ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]

def isAscending(lst):
    for i,v in enumerate(lst):
        if v!=ascending[i]:
            return False
    return True

def isDescending(lst):
    for i,v in enumerate(lst):
        if v!=ascending[7-i]:
            return False
    return True

if isAscending(lst):print("ascending")
elif isDescending(lst):print("descending")
else: print("mixed")